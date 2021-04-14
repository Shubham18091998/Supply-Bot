import cv2 as cv
import numpy as np
import os

img = cv.imread('color_image.jpg')
img_gray = cv.imread('color_image.jpg',0)
print ("Color image shape =", img.shape)
print ("Grayscale image shape =",img_gray.shape)
cv.namedWindow('color image')
cv.imshow('color image', img)
cv.waitKey(0)
cv.destroyWindow('color image')
cv.imshow('grayscale image', img_gray)
cv.waitKey(5000)
cv.imwrite('image_gray.jpg', img_gray)
cv.destroyAllWindows()
