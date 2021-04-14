import cv2 
import numpy as np
import os
import math
import csv
import copy

import cv2.aruco as aruco
from Other import *
from digi.xbee.devices import XBeeDevice


cap=cv2.VideoCapture(1)
ret,frame = cap.read()
#cv2.imshow("window2", frame)
#cv2.waitKey(1)
#fps = cap.get(cv2.CAP_PROP_FPS)
#print(fps)
#cap.set(1, fps*s)
#height, width, channels = frame.shape
#c2 =-1*(height/2)
#c1 =(width/2)

k=0
c1=255
c2=227
#print("Center of flex",c1,c2)
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
lower_red = np.array([170,100,100])
upper_red = np.array([179,255,255])
mask_red = cv2.inRange(hsv, lower_red, upper_red)
res_red = cv2.bitwise_and(frame, frame, mask=mask_red)
imgray = cv2.blur(res_red, (3,3))
threshold=400
canny_output=cv2.Canny(res_red, threshold, threshold*2)
contours, hierarchy = cv2.findContours(canny_output,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contour_list = []
for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 5 and len(approx) < 15)and (area > 70 and area < 110)):
                contour_list.append(contour)
x_red=contours[len(contours)-1][0][0][0]
y_red=(contours[len(contours)-1][0][0][1])
#print("Red coin center(x,y)=",x_red, y_red)

device = XBeeDevice("COM5", 9600)
device.open()
device.send_data_broadcast('F')
device.close()

angle1=10000.0
while(angle1>5):
        robot_state=0
        ret,frame = cap.read()
        det_aruco_list = {}
        det_aruco_list = detect_Aruco(frame)
        if det_aruco_list:
                img = mark_Aruco(frame,det_aruco_list)
                cv2.waitKey(25)
                #cv2.waitKey(0)
                robot_state = calculate_Robot_State(img,det_aruco_list)
                aruco_x=robot_state[(min(robot_state.keys()))][1]
                aruco_y=(robot_state[(min(robot_state.keys()))][2])
                #print("Aruco center(x,y)=",aruco_x,aruco_y)
                if(c1!=aruco_x):
                        m1=(c2-aruco_y)/(c1-aruco_x)
                if(c1!=x_red):
                        m2=(c2-y_red)/(c1-x_red)
                #angle=round(max(  math.degrees(math.atan((m1-m2)/(1+m1*m2)))  ,  math.degrees(math.atan((m2-m1)/(1+m1*m2))) ),2)
                angle1=(round(math.degrees(math.atan((m1-m2)/(1+m1*m2))),2))
                if (angle1<0):
                        angle1=angle1+180

                        
device = XBeeDevice("COM5", 9600)
device.open()
device.send_data_broadcast('S')
device.close()


device = XBeeDevice("COM5", 9600)
device.open()
device.send_data_broadcast('H')
device.close()


device = XBeeDevice("COM5", 9600)
device.open()
device.send_data_broadcast('F')
device.close()

angle1=10000.0
while(angle1>5):
        robot_state=0
        ret,frame = cap.read()
        det_aruco_list = {}
        det_aruco_list = detect_Aruco(frame)
        if det_aruco_list:
                img = mark_Aruco(frame,det_aruco_list)
                #cv2.imshow("window", img)
                robot_state = calculate_Robot_State(img,det_aruco_list)
                aruco_x=robot_state[(min(robot_state.keys()))][1]
                aruco_y=(robot_state[(min(robot_state.keys()))][2])
                #print("Aruco center(x,y)=",aruco_x,aruco_y)
                if(c1!=aruco_x):
                        m1=(c2-aruco_y)/(c1-aruco_x)
                if(c1!=x_red):
                        m2=(c2-y_red)/(c1-x_red)
                #angle=round(max(  math.degrees(math.atan((m1-m2)/(1+m1*m2)))  ,  math.degrees(math.atan((m2-m1)/(1+m1*m2))) ),2)
                angle1=(round(math.degrees(math.atan((m1-m2)/(1+m1*m2))),2))
                if (angle1<0):
                        angle1=angle1+180
        if(k==0):
                arr=np.array([[342,391],[221,362],[160,286],[158,170],[222,87],[299,57],[409,79],[490,171],[479,300]])
                minc=100000.0
                mina=111110.0
                start=0
                end=0
                i=0
                e_x=0
                e_y=0
                while(i<9):
                        if(math.sqrt((arr[i][0]-x_red)*(arr[i][0]-x_red)+(arr[i][1]-y_red)*(arr[i][1]-y_red))<minc):
                                end=i
                                minc=math.sqrt((arr[i][0]-x_red)*(arr[i][0]-x_red)+(arr[i][1]-y_red)*(arr[i][1]-y_red))
                        if(math.sqrt((arr[i][0]-aruco_x)*(arr[i][0]-aruco_x)+(arr[i][1]-aruco_y)*(arr[i][1]-aruco_y))<mina):
                                start=i
                                mina=math.sqrt((arr[i][0]-aruco_x)*(arr[i][0]-aruco_x)+(arr[i][1]-aruco_y)*(arr[i][1]-aruco_y))
                                e_x=arr[i][0]
                                e_y=arr[i][1]
                        i=i+1
                        k=0

#cv2.imshow("window2",frame)
#cv2.waitKey(1)
device = XBeeDevice("COM5", 9600)
device.open()
device.send_data_broadcast('S')
device.close()

print("Node number of city requiring the aid:", end+1)
cap.release()
cv2.destroyAllWindows()

        





