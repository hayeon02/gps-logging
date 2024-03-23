#!/usr/bin/env python
import rospy
import message_filters
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Quaternion, Point, Vector3, PoseStamped, Twist
from sensor_msgs.msg import Imu, NavSatFix
from morai_msgs.msg import EgoVehicleStatus, GPSMessage
from std_msgs.msg import Float64
import tf
from geodesy import utm

class IMUGPSToOdometry:
    def __init__(self):
        rospy.init_node('odom_converter')
        #목표 좌표 발행
        self.local_goal_pub = rospy.Publisher('/local_goal', PoseStamped, queue_size=10)
        # 목표까지 거리 발행
        self.dist_to_goal_pub = rospy.Publisher('/dist_to_goal_th', Float64, queue_size=10)
        # 목표 속력 발행
        self.target_velocity_pub = rospy.Publisher('/target_velocity', Twist, queue_size=10)
        rospy.Subscriber('/move_base_simple/goal', PoseStamped, self.goal_callback)
        self.distance = 0
        #self.dwa_target_velocity
        self.odom_pub = rospy.Publisher('odom', Odometry, queue_size=50)
        self.GPS_To_utm_pub = rospy.Publisher('/utm_gps', Point, queue_size=1)

        self.sub_gps = rospy.Subscriber('/gps', GPSMessage, self.gps_callback)

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
        #odom_msg.pose.pose.position = ego_data.position
        odom_msg.pose.pose.position.x = 0
        odom_msg.pose.pose.position.y = 0
        odom_msg.pose.pose.position.z = 0
        odom_msg.twist.twist.linear = ego_data.velocity

        self.odom_pub.publish(odom_msg)


    def goal_callback(self, msg):

        # 받은 목표(goal) 메시지를 /local_goal 토픽으로 재발행
        print("goal :", msg)
        self.distance = (msg.pose.position.x**2 + msg.pose.position.y**2) ** (0.5)
        
        self.local_goal_pub.publish(msg)
    def gps_callback(self, data) :
        # GPS 데이터 처리
        utm_coord = utm.fromLatLong(data.latitude, data.longitude).toPoint()
        pub = Point(utm_coord.x, utm_coord.y, 0)  # z는 고도 정보 사용 시 수정 가능
        self.GPS_To_utm_pub.publish(pub)
        target_vel = Twist()
        target_vel.linear.x = 1

        self.target_velocity_pub.publish(target_vel)
        self.dist_to_goal_pub.publish(self.distance)
if __name__ == '__main__':

    synced_publisher = IMUGPSToOdometry()
    rospy.spin()