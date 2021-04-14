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




########################################################################
## using os to generalise Input-Output
########################################################################
codes_folder_path = os.path.abspath('.')
images_folder_path = os.path.abspath(os.path.join('..', 'Images'))
generated_folder_path = os.path.abspath(os.path.join('..', 'Generated'))




############################################
## Build your algorithm in this function
## ip_image: is the array of the input image
## imshow helps you view that you have loaded
## the corresponding image
############################################
def process(ip_image):
    ###########################
    ## Your Code goes here
    height, width, channels = ip_image.shape
    c1 = height/2
    c2 = -1*(width/2)
    green  = ip_image[:,:,1]
    red = ip_image[:,:,2]
    xr=1025
    xxr=-1
    yr=1025
    yyr=-1
    xg=1025
    xxg=-1
    yg=1025
    yyg=-1
    for i in range(1023):
      for j in range(1023):
        if ((red[i,j] == 255) and (green[i,j]==0)):
            xr=min(xr,i)
            xxr=max(xxr,i)
            yr=min(yr,j)
            yyr=max(yyr,j)
        if ((red[i,j] == 0) and (green[i,j]==255)):
            xg=min(xg,i)
            xxg=max(xxg,i)
            yg=min(yg,j)
            yyg=max(yyg,j)
    x1=xr+(xxr-xr)/2
    y1=-1*(yr+(yyr-yr)/2)
    x2=xg+(xxg-xg)/2
    y2=-1*(yg+(yyg-yg)/2)
    m1=(c2-y1)/(c1-x1)
    m2=(c2-y2)/(c1-x2)
    angle=180-round(max(  math.degrees(math.atan((m1-m2)/(1+m1*m2)))  ,  math.degrees(math.atan((m2-m1)/(1+m1*m2)))  ),2)
    ## Your Code goes here
    ###########################
    cv2.imshow("window", ip_image)
    cv2.waitKey(0);
    return angle




    
####################################################################
## The main program which provides read in input of one image at a
## time to process function in which you will code your generalized
## output computing code
## Do not modify this code!!!
####################################################################
def main():
    ################################################################
    ## variable declarations
    ################################################################
    i = 1
    line = []
    ## Reading 1 image at a time from the Images folder
    for image_name in os.listdir(images_folder_path):
        ## verifying name of image
        print(image_name)
        ## reading in image 
        ip_image = cv2.imread(images_folder_path+"/"+image_name)
        ## verifying image has content
        print(ip_image.shape)
        ## passing read in image to process function
        A = process(ip_image)
        ## saving the output in  a list variable
        line.append([str(i), image_name , str(A)])
        ## incrementing counter variable
        i+=1
    ## verifying all data
    print(line)
    ## writing to angles.csv in Generated folder without spaces
    with open(generated_folder_path+"/"+'angles.csv', 'w', newline='') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerows(line)
    ## closing csv file    
    writeFile.close()



    

############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main()
