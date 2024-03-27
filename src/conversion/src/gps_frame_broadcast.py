#!/usr/bin/env python
import rospy
import tf2_ros
import utm
from geometry_msgs.msg import TransformStamped, Point
from morai_msgs.msg import GPSMessage

def callback(position):
    # 위도와 경도를 UTM 좌표로 변환
    # utm_coords = utm.from_latlon(msg.latitude, msg.longitude)
    # easting, northing, zone_number, zone_letter = utm_coords
    
    # TF 변환 생성
    t = TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "gps_utm"
    t.child_frame_id = "odom"
    
    # 변환된 UTM 좌표를 사용하여 변환 위치 설정
    t.transform.translation.x = position.x
    t.transform.translation.y = position.y
    t.transform.translation.z = 0# 고도 정보 사용
    
    # 회전 정보 설정 (여기서는 단위 회전)
    t.transform.rotation.x = 0
    t.transform.rotation.y = 0
    t.transform.rotation.z = 0
    t.transform.rotation.w = 1
    
    # TF 방송
    br.sendTransform(t)

if __name__ == '__main__':
    rospy.init_node('gps_tf_broadcaster')
    br = tf2_ros.TransformBroadcaster()
    rospy.Subscriber("/relative_position", Point, callback)
    rospy.spin()