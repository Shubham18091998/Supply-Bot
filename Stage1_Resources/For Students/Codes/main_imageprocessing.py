import cv2 as cv
import numpy as np
import os

def partA(file):
    img = cv.imread(file)
    basename = os.path.basename(file)
    height, width, channels = img.shape
    h = round(height/2)
    w = round(width/2)
    px = img[h,w]
    return np.array([basename, height, width, channels, px[0], px[1], px[2]])
    pass

def partB(file):
    img = cv.imread(file)
    img[:,:,0] = 0
    img[:,:,1] = 0
    cv.imwrite(os.path.join(dirname, 'Generated/coldautumn_red1.jpg'),img)
    pass

def partC(file):
    img = cv.imread(file)
    img_alpha = cv.cvtColor(img, cv.COLOR_BGR2BGRA)
    img_alpha[:,:,3] = 127
    cv.imwrite(os.path.join(dirname, 'Generated/flower_alpha1.png'), img_alpha)
    pass

def partD(file):
    img = cv.imread(file)
    #gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    height, width = img.shape[:2]
    gray = np.zeros((height,width), dtype = np.uint8)
    for i in range (height):
        for j in range (width):
            pxl_b = img[i,j,0]
            pxl_g = img[i,j,1]
            pxl_r = img[i,j,2]
            intensity = ((0.3*pxl_r)+(0.59*pxl_g)+(0.11*pxl_b))
            gray[i,j] = round(intensity)
    cv.imwrite(os.path.join(dirname, 'Generated/landscape1_gray.jpg'), gray)
    pass

dirname = os.path.dirname(os.path.dirname(__file__))

a = partA(os.path.join(dirname, 'Sample Input Images/beauty.jpg').replace('\\','/'))
b = partA(os.path.join(dirname, 'Sample Input Images/coldautumn.jpg').replace('\\','/'))
c = partA(os.path.join(dirname, 'Sample Input Images/flower.jpg').replace('\\','/'))
d = partA(os.path.join(dirname, 'Sample Input Images/landscape.jpg').replace('\\','/'))
np.savetxt(os.path.join(dirname, 'Generated/stats1.csv'), np.stack((a, b, c, d)), delimiter=",", fmt='%s')

partB(os.path.join(dirname, 'Sample Input Images/coldautumn.jpg').replace('\\','/'))

partC(os.path.join(dirname, 'Sample Input Images/flower.jpg').replace('\\','/'))

partD(os.path.join(dirname, 'Sample Input Images/landscape.jpg').replace('\\','/'))
