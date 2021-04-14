###############################################################################
## Author: Team Supply Bot
## Edition: eYRC 2019-20
## Instructions: Do Not modify the basic skeletal structure of given APIs!!!
###############################################################################


######################
## Essential libraries
######################
import cv2
import numpy as np
import os
import math
import csv
import copy






############################################
## Build your algorithm in this function
## ip_image: is the array of the input image
## imshow helps you view that you have loaded
## the corresponding image
############################################
def process(ip_image):
    ###########################
    ## Your Code goes here
    ###########################
    op_image = ip_image
    height, width, channels = ip_image.shape
    c1 = height/2
    c2 = -1*(width/2)
    #c1=319
    #c2=-242
    hsv = cv2.cvtColor(ip_image, cv2.COLOR_BGR2HSV)
    lower_green = np.array([40,100,100])
    upper_green = np.array([70,255,255])
    mask_green = cv2.inRange(hsv, lower_green, upper_green)
    res_green = cv2.bitwise_and(ip_image, ip_image, mask=mask_green)
    lower_red = np.array([170,100,100])
    upper_red = np.array([179,255,255])
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    res_red = cv2.bitwise_and(ip_image, ip_image, mask=mask_red)
    dst = cv2.addWeighted(res_red, 1.0, res_green, 1.0, 0.0)
    imgray = cv2.blur(dst, (3,3))
    threshold=400
    canny_output=cv2.Canny(dst, threshold, threshold*2)
    #cv2.imshow('canny_output', canny_output)
    contours, hierarchy = cv2.findContours(canny_output,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #print(contours)
    contour_list = []
    for contour in contours:
        approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour,True),True)
        area = cv2.contourArea(contour)
        if ((len(approx) > 5 and len(approx) < 15)and (area > 70 and area < 110)):
            contour_list.append(contour)
    #print(contour_list)   
    img = cv2.drawContours(ip_image, contours, 0, (255,0,0), 2)
    img = cv2.drawContours(ip_image, contours, len(contours)-1, (255,0,0), 2)
    #cv2.imshow('window', img)
    x1=contours[len(contours)-1][0][0][0]
    y1=-1*(contours[len(contours)-1][0][0][1])
    x2=contours[0][0][0][0]
    y2=-1*(contours[0][0][0][1])
    m1=(c2-y1)/(c1-x1)
    m2=(c2-y2)/(c1-x2)
    angle=180-round(max(  math.degrees(math.atan((m1-m2)/(1+m1*m2)))  ,  math.degrees(math.atan((m2-m1)/(1+m1*m2)))  ),2)
    org=(50,50)
    font=cv2.FONT_HERSHEY_SIMPLEX
    fontScale=0.5
    color=(0,0,255)
    thickness=1
    cv2.putText(ip_image, str(angle), org, font, fontScale, color, thickness, cv2.LINE_AA) 
    return ip_image

    
####################################################################
## The main program which provides read in input of one image at a
## time to process function in which you will code your generalized
## output computing code
## Modify the image name as per instruction
####################################################################
def main():
    ################################################################
    ## variable declarations
    ################################################################
    i = 1
    ## reading in video 
    cap = cv2.VideoCapture(0) #if you have a webcam on your system, then change 0 to 1
    ## getting the frames per second value of input video
    fps = cap.get(cv2.CAP_PROP_FPS)
    ## setting the video counter to frame sequence
    cap.set(3, 640)
    cap.set(4, 480)
    cap.set(1, fps*10)
    ## reading in the frame
    ret, frame = cap.read()
    ## verifying frame has content
    print(frame.shape)
    while(ret):
        ret, frame = cap.read()
        ## display to see if the frame is correct
        cv2.imshow("window", frame)
        cv2.waitKey(int(1000/fps));
        ## calling the algorithm function
        op_image = process(frame)
        cv2.imwrite("SB#2726_task3I.jpg",op_image)
        cap.release()


    

############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main()
