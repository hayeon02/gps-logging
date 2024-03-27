#!/usr/bin/env python
import rospy
from visualization_msgs.msg import Marker
from geometry_msgs.msg import PoseStamped

def publish_marker(goal):
    rospy.init_node('utm_marker_publisher', anonymous=True)
    
    # Marker publisher 초기화
    pub = rospy.Publisher('visualization_marker', Marker, queue_size=10)
    
    # Marker 메시지 설정
    marker = Marker()
    marker.header.frame_id = "gps_utm"  # 마커가 배치될 좌표계
    marker.header.stamp = rospy.Time.now()
    marker.ns = "utm"
    marker.id = 0
    marker.type = Marker.SPHERE  # 마커의 형태
    marker.action = Marker.ADD  # 마커 추가
    marker.pose.position.x = goal.x  # UTM x 좌표
    marker.pose.position.y = goal.y  # UTM y 좌표
    marker.pose.position.z = 0  # 마커의 z 위치 (고도)
    marker.pose.orientation.x = 0.0
    marker.pose.orientation.y = 0.0
    marker.pose.orientation.z = 0.0
    marker.pose.orientation.w = 1.0
    marker.scale.x = 1.0  # 마커의 크기
    marker.scale.y = 1.0
    marker.scale.z = 1.0
    marker.color.a = 1.0  # 마커의 색상과 투명도
    marker.color.r = 1.0
    marker.color.g = 0.0
    marker.color.b = 0.0
    
    # Marker 발행
    while not rospy.is_shutdown():
        pub.publish(marker)
        rospy.sleep(1)

if __name__ == '__main__':
    try:
        rospy.init_node("Goal_visualization")
        rospy.Subscriber('/local_goal', PoseStamped, publish_marker)
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
