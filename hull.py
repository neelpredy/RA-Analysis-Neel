import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    #successRead, frames = cap.read()
    #imageInput = cv2.imread("C:/Users/Neel/Documents/GitHub/RA-detection/backhand.jpg")
    
    success, imageInput = cap.read()
    
    cv2.imshow('SrcInput', imageInput)

    gray = cv2.cvtColor(imageInput, cv2.COLOR_BGR2GRAY) # convert to grayscale
    ret, thresh = cv2.threshold(gray, 125, 255, 0)   

    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1500:
            accuracy = 0.0001 * cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, accuracy, True)
            imgContour = cv2.drawContours(imageInput, [approx], -1, (255, 0, 0), 3)
    
    #imgContour = cv2.drawContours(imageInput, contours, -1, (0, 255, 0), 3)

    for contour in contours:
        hull = cv2.convexHull(contour)
        imgconvexHull = cv2.drawContours(imageInput, [hull], 0, (255, 255, 0), 2)
        

    cv2.imshow('thresh', thresh)
    #cv2.imshow('contour', imgContour)
    cv2.imshow('convexHull', imgconvexHull)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()