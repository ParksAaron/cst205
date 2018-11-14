import numpy as np
import cv2
# convert image to grayscale
im_gray = cv2.imread('background.jpg', cv2.IMREAD_GRAYSCALE)
# use highgui to display image
cv2.imshow("Jeanne in Gray", im_gray)
# keeps the image displayed
cv2.waitKey()