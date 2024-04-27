#!/usr/bin/env python3
import os
import folium
import csv

with open('1_5_Waypoint_WGS84.csv') as csv_file:
    data = csv.reader(csv_file)

    seq = []
    latitude = []
    longitude = []

    for i in data:
        seq.append(int(i[0]))
        latitude.append(float(i[2]))
        longitude.append(float(i[1]))

    api_key = "c8a0cb28-5b5d-42eb-850f-6a7888cef473"
    gps_map = folium.Map(location=[latitude[0], longitude[0]], zoom_start=20)
    for j in range(len(seq)):
        folium.PolyLine(locations=[[latitude[j], longitude[j]], [latitude[j], longitude[j]]], color='blue', weight=3, tooltip='polyline').add_to(gps_map)
    folium.Marker([latitude[j], longitude[j]], popup=seq[j], icon=folium.Icon(color="blue", icon="star")).add_to(gps_map)
    gps_map.save('test.html')

if os.path.exists("test.html"):
    print("gps_map saved")
else:
    print("gps_map not saved")
