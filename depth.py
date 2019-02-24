import numpy as np
import cv2
from matplotlib import pyplot as plt

img_l = cv2.imread("C:/Users/Neel/Desktop/python/neel_hand_l.jpg",0)
img_r = cv2.imread("C:/Users/Neel/Desktop/python/neel_hand_r.jpg",0)
stereo = cv2.StereoBM_create(numDisparities=16, blockSize=7)
disparity = stereo.compute(img_l,img_r)
plt.imshow(disparity)
plt.show()   