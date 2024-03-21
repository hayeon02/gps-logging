#!/usr/bin/env python
import rospy
import message_filters
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Point, Vector3, PoseStamped
from sensor_msgs.msg import Imu, NavSatFix
from morai_msgs.msg import EgoVehicleStatus
import tf
from geodesy import utm

class IMUGPSToOdometry:
    def __init__(self):
        rospy.init_node('odom_converter')
        self.local_goal_pub = rospy.Publisher('/local_goal', PoseStamped, queue_size=10)
        rospy.Subscriber('/move_base_simple/goal', PoseStamped, self.goal_callback)

        self.odom_pub = rospy.Publisher('odom', Odometry, queue_size=50)
        self.GPS_To_utm_pub = rospy.Publisher('/utm_gps', Point, queue_size=1)

        self.sub_gps = rospy.Subscriber('/gps', EgoVehicleStatus, self.gps_callback)

        self.imu_sub = message_filters.Subscriber('/imu', Imu)
        self.Ego_status_sub = message_filters.Subscriber('/Ego_topic', EgoVehicleStatus)
        
        self.ts = message_filters.ApproximateTimeSynchronizer([self.imu_sub, self.Ego_status_sub], queue_size=10, slop=0.5, allow_headerless=True)
        self.ts.registerCallback(self.callback)
        
    def callback(self, imu_data, ego_data) :
        odom_msg = Odometry()
        odom_msg.header.stamp = rospy.Time.now()
        odom_msg.header.frame_id = "odom"
        odom_msg.child_frame_id = "base_link"

        odom_msg.pose.pose.orientation = imu_data.orientation
        odom_msg.twist.twist.angular = imu_data.angular_velocity
        odom_msg.pose.pose.position = ego_data.position
        odom_msg.twist.twist.linear = ego_data.velocity

        self.odom_pub.publish(odom_msg)

    def gps_callback(self, data) :
        # GPS 데이터 처리
        utm_coord = utm.fromLatLong(data.latitude, data.longitude).toPoint()
        pub = Point(utm_coord.x, utm_coord.y, 0)  # z는 고도 정보 사용 시 수정 가능
        self.GPS_To_utm_pub.publish(pub)
    def goal_callback(self, msg):
        # 받은 목표(goal) 메시지를 /local_goal 토픽으로 재발행
        print("goal :", msg)
        self.local_goal_pub.publish(msg)
if __name__ == '__main__':

    synced_publisher = IMUGPSToOdometry()
    rospy.spin()