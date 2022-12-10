import cv2 as cv
import numpy as np

from rich.traceback import install
install(show_locals = True)

cam = cv.VideoCapture(0)

while True:
    _, frame = cam.read()
    
    #cv.imshow("Camera Feed", frame)
    #
    #laplacian = cv.Laplacian(frame, cv.CV_64F)
    #laplacian = np.uint8(laplacian)
    #cv.imshow("Laplacian Effect", laplacian)
    
    edges = cv.Canny(frame, 100, 100)
    cv.imshow("Edges Effect", edges)
    
    if cv.waitKey(5) == ord("q"):
        break

cam.release()
cv.destroyAllWindows()