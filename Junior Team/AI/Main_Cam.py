import numpy as np
import cv2
img = cv2.imread('Pictures/image.png')
blur = cv2.GaussianBlur(img, (7, 7), 2)
h, w = img.shape[:2]
# Morphological gradient
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
gradient = cv2.morphologyEx(blur, cv2.MORPH_GRADIENT, kernel)
cv2.imshow('Morphological gradient', gradient)
cv2.waitKey()