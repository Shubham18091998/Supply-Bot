import  cv2 as cv
import numpy as np
import os

cap = cv.VideoCapture(0)
while(1):
    ret, frame = cap.read()
    cv.imshow('captured frame', frame)
    if cv.waitKey(1)==27:
        cv.imwrite('captured frame.png', frame)
        break

cap.release()
cv.destroyAllWindows()


