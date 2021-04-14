import cv2 as cv
import numpy as np
import os

cap = cv.VideoCapture(0)
ret, frame = cap.read()
cv.imshow('Captured Image', frame)
cv.waitKey(0)
cap.release()
cv.destroyAllWindows()
