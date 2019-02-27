import cv2
import numpy as np

while True:
    imageInput = cv2.imread("C:/Users/neel_pupreddiwar/Documents/GitHub/RA-detection/ra4.jpg",0)
    
    #convert to hsv
    hsv_img = cv2.cvtColor(imageInput, cv2.COLOR_BGR2HSV)

    #convert to threshhold
    ret, thresh = cv2.threshold(hsv_img, 125, 255, 0)

    #compute Hough circle
    hough_image = cv2.HoughCircles(thresh, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    
    #print(hough_image)
    cv2.imshow('output',hough_image)

    k = cv2.waitKey(1)
    if k == 27:
        break
