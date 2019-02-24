import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2

cam = cv2.VideoCapture(0)

while True:
    success, img = cam.read()

    #img = mpimg.imread("C:/Users/Neel/Documents/GitHub/RA-detection/ra3.jpg")

    lum_img = img[:,:,0]

    imgplot = plt.imshow(lum_img)
    imgplot.set_cmap('nipy_spectral')

    plt.colorbar()
    plt.show()
