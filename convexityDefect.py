import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    success, imageInput = cap.read()

    gray = cv2.cvtColor(imageInput, cv2.COLOR_BGR2GRAY) # convert to grayscale
    ret, thresh = cv2.threshold(gray, 125, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
    
    cv2.imshow('SrcInput', imageInput)
    cv2.imshow('Thresh', thresh)
    
    defects = []
    for contour in contours:
        hull = cv2.convexHull(contour,returnPoints = False)
        defects = cv2.convexityDefects(contour,hull)
    
    #print(defects)
    '''
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start = tuple(contours[s][0])
        end = tuple(contours[e][0])
        far = tuple(contours[f][0])
        cv2.line(imageInput,start,end,[0,255,0],2)
        cv2.circle(imageInput,far,5,[0,0,255],-1)
    '''
    #cv2.imshow('SrcInputDefects', imageInput)

    k = cv2.waitKey(1)
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()