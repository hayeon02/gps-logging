#!/usr/bin/env python
import rospy
import message_filters
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Point, Vector3, PoseStamped, Twist
from sensor_msgs.msg import Imu, NavSatFix
from morai_msgs.msg import EgoVehicleStatus, GPSMessage
from std_msgs.msg import Float64

import tf
import utm
import time

class IMUGPSToOdometry:
    def __init__(self):
        rospy.init_node('odom_converter')
        #목표 좌표 발행
        self.local_goal_pub = rospy.Publisher('/local_goal', PoseStamped, queue_size=10)
        # 목표까지 거리 발행
        self.dist_to_goal_pub = rospy.Publisher('/dist_to_goal_th', Float64, queue_size=10)
        # 현재 utm좌표 발행
        self.current_utm_position = rospy.Publisher('/current_utm_position', Point, queue_size=10)
        
        self.relative_position = rospy.Publisher('/relative_position', Point, queue_size=10)
        self.init_position_flag = True
        self.init_position = Point()

        # 목표 속력 발행
        self.target_velocity_pub = rospy.Publisher('/target_velocity', Twist, queue_size=10)
        rospy.Subscriber('/move_base_simple/goal', PoseStamped, self.goal_pub)
        self.distance = 0
        #self.dwa_target_velocity
        self.odom_pub = rospy.Publisher('odom', Odometry, queue_size=50)
        self.GPS_To_utm_pub = rospy.Publisher('/utm_gps', Point, queue_size=1)

        self.sub_gps = message_filters.Subscriber('/gps', GPSMessage)
        self.imu_sub = message_filters.Subscriber('/imu', Imu)
        self.Ego_status_sub = message_filters.Subscriber('/Ego_topic', EgoVehicleStatus)
        
        self.ts = message_filters.ApproximateTimeSynchronizer([self.imu_sub, self.Ego_status_sub, self.sub_gps], queue_size=10, slop=0.5, allow_headerless=True)
        self.ts.registerCallback(self.callback)
        
    def callback(self, imu_data, ego_data, gps_data) :
        
        utm_coords = utm.from_latlon(gps_data.latitude, gps_data.longitude)
        easting, northing, zone_number, zone_letter = utm_coords
        if self.init_position_flag :
            time.sleep(2)
            
            self.init_position.x = easting
            self.init_position.y = northing
            self.init_position.z = 0
            
            rospy.loginfo("Set init position")
            self.init_position_flag = False

        odom_msg = Odometry()
        odom_msg.header.stamp = rospy.Time.now()
        odom_msg.header.frame_id = "odom"
        odom_msg.child_frame_id = "base_link"

        # 현재 위치 (UTM좌표계)
        current_utm_position = Point()
        current_utm_position.x = easting - self.init_position.x
        current_utm_position.y = northing - self.init_position.y
        current_utm_position.z = 0
        
        # 현재 위치 odom에 대입
        odom_msg.pose.pose.orientation = imu_data.orientation
        odom_msg.twist.twist.angular = imu_data.angular_velocity
        #odom_msg.pose.pose.position = ego_data.position
        odom_msg.pose.pose.position.x = current_utm_position.x
        odom_msg.pose.pose.position.y = current_utm_position.y
        odom_msg.pose.pose.position.z = 0

        odom_msg.twist.twist.linear = ego_data.velocity

        self.relative_position.publish(current_utm_position) 
        self.current_utm_position.publish(current_utm_position)

        self.odom_pub.publish(odom_msg)
    

    def goal_pub(self, msg):

        self.local_goal_pub.publish(msg)
if __name__ == '__main__':

    synced_publisher = IMUGPSToOdometry()
    rospy.spin()