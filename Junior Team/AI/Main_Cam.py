import numpy as np
import cv2

from rich.traceback import install
install(show_locals=True)

img = cv2.imread("C:\\Users\\hadir\\Documents\\VSC - Projects\\DEWA-AI-Comp\\Junior Team\\Pictures\\pipe#2.jpg", 1)

blur = cv2.GaussianBlur(img, (7, 7), 2)
h, w = img.shape[:2]

# Binarize gradient

kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (4, 4))
gradient = cv2.morphologyEx(blur, cv2.MORPH_GRADIENT, kernel)

lowerb = np.array([0, 0, 0])
upperb = np.array([15, 15, 15])
binary = cv2.inRange(gradient, lowerb, upperb)
cv2.imshow('Binarized gradient', binary)
cv2.waitKey()