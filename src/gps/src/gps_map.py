#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import NavSatFix
import pandas as pd
import datetime
import utm
import math
import os
import folium

df = pd.DataFrame(columns = ['seq', 'llatitude', 'longitude', 'llatitude_utm', 'longitude_utm']) #csv colums

#previous_latitude, previous_longitude reset
previous_latitude = 0
previous_longitude = 0

save_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') #csv file name
csv_name = save_time + '.csv'

gps_map = folium.Map(location=[0, 0], zoom_start=20)

points = []

def map(msg):
    global gps_map
    gps_map = folium.Map(location=[msg.latitude, msg.longitude], zoom_start=20)
    folium.Marker([msg.latitude, msg.longitude], popup=[msg.latitude, msg.longitude], icon=folium.Icon(color="blue", icon="star")).add_to(gps_map)
    gps_map.save('map.html')
    

def gps_callback(msg):
    #gps variable
    global previous_latitude, previous_longitude, points
    seq: int = msg.header.seq
    latitude: float = msg.latitude
    longitude: float = msg.longitude

    #change utm
    utm_gps = utm.from_latlon(latitude, longitude)
    
    llatitude_utm: float = utm_gps[0] 
    longitude_utm: float = utm_gps[1]

    #utm value distance calculation
    distance = math.sqrt((llatitude_utm - previous_latitude)**2 + (longitude_utm - previous_longitude)**2)
    
    if previous_latitude == 0 and previous_longitude == 0:
        previous_latitude = llatitude_utm
        previous_longitude = longitude_utm
    else:
        if distance >= 0.2: #distance save condition
            rospy.loginfo("seq: {}, latitude: {}, longitude {}".format(seq, latitude, longitude))
            rospy.loginfo(distance)
            df.loc[len(df)] = [seq, latitude, longitude, llatitude_utm, longitude_utm]
            points.append([latitude, longitude])
            folium.Marker([latitude, longitude], popup=points, icon=folium.Icon(color="blue", icon="star")).add_to(gps_map)
            folium.PolyLine(locations=points, color='blue', weight=3, tooltip='polyline').add_to(gps_map)
            gps_map.save('map.html')
            previous_latitude = llatitude_utm
            previous_longitude = longitude_utm
    
    df.to_csv(csv_name, index = False)

if __name__ == '__main__':
    rospy.init_node('gps_data')
    rospy.Subscriber('/ublox_gps/fix', NavSatFix, map, queue_size=1)
    rospy.Subscriber('/ublox_gps/fix', NavSatFix, gps_callback)
    rospy.spin()
    if os.path.exists(csv_name):
        print("csv파일이 저장되었습니다.")
    else:
        print("csv파일이 저장되지 않았습니다.")