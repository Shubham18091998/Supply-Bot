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
import cv2.aruco as aruco
from aruco_lib import *
import copy



########################################################################
## using os to generalise Input-Output
########################################################################
codes_folder_path = os.path.abspath('.')
images_folder_path = os.path.abspath(os.path.join('..', 'Videos'))
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
    ###########################

    def blur_edge(img, d=10):
        height,width=img.shape[:2]
        img_pad=cv2.copyMakeBorder(img,d,d,d,d,cv2.BORDER_WRAP)
        img_blur=cv2.GaussianBlur(img_pad,(d+1,d+1),-1)[d:-d,d:-d]
        y,x=np.indices((height,width))
        distance=np.dstack([x,width-x-1,y,height-y-1]).min(-1)
        width=np.minimum(np.float32(distance)/d,1.0)
        return img*width+img_blur*(1-width)

    def motion_kernel(angle,d,size=50):
        kern=np.ones((1,d),np.float32)
        cosine,sine=np.cos(angle),np.sin(angle)
        A=np.float32([[cosine,-sine,0],[sine,cosine,0]])
        size2=size//2
        A[:,2]=(size2,size2)-np.dot(A[:,:2], ((d-1)*0.5,0))
        kern = cv2.warpAffine(kern, A, (size, size), flags=cv2.INTER_CUBIC)
        return kern

    b,g,r=cv2.split(ip_image)
    b=np.float32(b)/255.0
    g=np.float32(g)/255.0
    r=np.float32(r)/255.0
    b=blur_edge(b)
    g=blur_edge(g)
    r=blur_edge(r)
    B=cv2.dft(b, flags=cv2.DFT_COMPLEX_OUTPUT)
    G=cv2.dft(g, flags=cv2.DFT_COMPLEX_OUTPUT)
    R=cv2.dft(r, flags=cv2.DFT_COMPLEX_OUTPUT)
    ang=np.deg2rad(90)
    d=19
    noise=10**(-0.1*25)
    psf_b=motion_kernel(ang,d)
    psf_g=motion_kernel(ang,d)
    psf_r=motion_kernel(ang,d)
    psf_b/=psf_b.sum()
    psf_g/=psf_g.sum()
    psf_r/=psf_r.sum()
    psf_pad_b=np.zeros_like(b)
    psf_pad_g=np.zeros_like(g)
    psf_pad_r=np.zeros_like(r)
    kh_b,kw_b=psf_b.shape
    kh_g,kw_g=psf_g.shape
    kh_r,kw_r=psf_r.shape
    psf_pad_b[:kh_b, :kw_b]=psf_b
    psf_pad_g[:kh_g, :kw_g]=psf_g
    psf_pad_r[:kh_r, :kw_r]=psf_r
    PSF_B=cv2.dft(psf_pad_b, flags=cv2.DFT_COMPLEX_OUTPUT, nonzeroRows=kh_b)
    PSF_G=cv2.dft(psf_pad_g, flags=cv2.DFT_COMPLEX_OUTPUT, nonzeroRows=kh_g)
    PSF_R=cv2.dft(psf_pad_r, flags=cv2.DFT_COMPLEX_OUTPUT, nonzeroRows=kh_r)
    PSF2_B=(PSF_B**2).sum(-1)
    PSF2_G=(PSF_G**2).sum(-1)
    PSF2_R=(PSF_R**2).sum(-1)
    iPSF_B=PSF_B/(PSF2_B+noise)[...,np.newaxis]
    iPSF_G=PSF_G/(PSF2_G+noise)[...,np.newaxis]
    iPSF_R=PSF_R/(PSF2_R+noise)[...,np.newaxis]
    RES_B=cv2.mulSpectrums(B, iPSF_B, 0)
    RES_G=cv2.mulSpectrums(G, iPSF_G, 0)
    RES_R=cv2.mulSpectrums(R, iPSF_R, 0)
    res_b=cv2.idft(RES_B, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
    res_g=cv2.idft(RES_G, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
    res_r=cv2.idft(RES_R, flags=cv2.DFT_SCALE | cv2.DFT_REAL_OUTPUT)
    res_b=np.roll(res_b, -kh_b//2, 0)
    res_g=np.roll(res_g, -kh_g//2, 0)
    res_r=np.roll(res_r, -kh_r//2, 0)
    res_b=np.roll(res_b, -kw_b//2, 1)
    res_g=np.roll(res_g, -kw_g//2, 1)
    res_r=np.roll(res_r, -kw_r//2, 1)

    
    image1=cv2.merge((res_b,res_g,res_r))
    image1=np.clip((image1*255),0,255)
    image2=image1.astype(np.uint8)

    img=np.zeros(image2.shape, image2.dtype)
    alpha=2.5
    beta = 0
    img=cv2.convertScaleAbs(image2, alpha=alpha, beta=beta)
    
    aruco_list=detect_Aruco(img)
    img=mark_Aruco(img,aruco_list)
    robot_state=calculate_Robot_State(img,aruco_list)
    cv2.imwrite(generated_folder_path+"/"+'aruco_with_id.png', img)
    robot_state_list=list(robot_state.items())
    r_s_l=robot_state_list[0][1]
    id_list =[r_s_l[0],r_s_l[1],r_s_l[2],r_s_l[3]]
    #cv2.imshow('deconvolution', img)
    return ip_image, id_list


    
####################################################################
## The main program which provides read in input of one image at a
## time to process function in which you will code your generalized
## output computing code
## Do not modify this code!!!
####################################################################
def main(val):
    ################################################################
    ## variable declarations
    ################################################################
    i = 1
    ## reading in video 
    cap = cv2.VideoCapture(images_folder_path+"/"+"arUco_bot.mp4")
    ## getting the frames per second value of input video
    fps = cap.get(cv2.CAP_PROP_FPS)
    ## getting the frame sequence
    frame_seq = int(val)*fps
    ## setting the video counter to frame sequence
    cap.set(1,frame_seq)
    ## reading in the frame
    ret, frame = cap.read()
    ## verifying frame has content
    print(frame.shape)
    ## display to see if the frame is correct
    cv2.imshow("window", frame)
    cv2.waitKey(0);
    ## calling the algorithm function
    op_image, aruco_info = process(frame)
    ## saving the output in  a list variable
    line = [str(i), "Aruco_bot.jpg" , str(aruco_info[0]), str(aruco_info[3])]
    ## incrementing counter variable
    i+=1
    ## verifying all data
    print(line)
    ## writing to angles.csv in Generated folder without spaces
    with open(generated_folder_path+"/"+'output.csv', 'w') as writeFile:
        print("About to write csv")
        writer = csv.writer(writeFile)
        writer.writerow(line)
    ## closing csv file    
    writeFile.close()



    

############################################################################################
## main function
############################################################################################
if __name__ == '__main__':
    main(input("time value in seconds:"))
