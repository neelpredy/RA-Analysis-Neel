import cv2
import numpy as np


imageInput = cv2.imread("C:/Users/neel_pupreddiwar/Documents/GitHub/RA-detection/eye1.jpg",1)
imgGray = cv2.cvtColor(imageInput,cv2.COLOR_BGR2GRAY)
imgGray = cv2.medianBlur(imgGray, 5)
cv2.imshow('bgr',imgGray)

rows = imgGray.shape[0]

circles = cv2.HoughCircles(imgGray,cv2.HOUGH_GRADIENT,1,rows / 8,
                        param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    center = (i[0], i[1])
    # circle center
    cv2.circle(imgGray, center, 1, (0, 100, 100), 3)
    # circle outline
    radius = i[2]
    cv2.circle(imgGray, center, radius, (255, 0, 255), 3)

cv2.imshow('detected circles',imgGray)

cv2.waitKey(0)
cv2.destroyAllWindows()