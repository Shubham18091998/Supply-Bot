import cv2 as cv
import numpy as np
import os

def partA(file):
    cap = cv.VideoCapture(file)
    cap.set(1, 151)
    ret, frame = cap.read()
    cv.imwrite(os.path.join(dirname, 'Generated/frame_as_6.jpg'), frame)
    cap.release()
    pass

def partB(file):
    img = cv.imread(file)
    img[:,:,0] = 0
    img[:,:,1] = 0
    cv.imwrite(os.path.join(dirname, 'Generated/frame_as_6_red.jpg'), img)
    pass

dirname = os.path.dirname(os.path.dirname(__file__))

partA(os.path.join(dirname, 'Videos/RoseBloom.mp4').replace('\\', '/'))

partB(os.path.join(dirname, 'Generated/frame_as_6.jpg').replace('\\', '/'))
