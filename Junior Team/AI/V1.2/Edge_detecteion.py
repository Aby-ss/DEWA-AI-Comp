import cv2 
import numpy as np

from cv2 import VideoWriter
from cv2 import VideoWriter_fourcc

from rich.traceback import install
install(show_locals = True)



cap = cv2.VideoCapture(0)  

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

# loop runs if capturing has been initialized. 
while(True):
    # reads frames from a camera 
    # ret checks return at each frame
    ret, frame = cap.read() 

    # Converts to grayscale space, OCV reads colors as BGR
    # frame is converted to gray
    gray = cv2.Canny(frame, 100, 100)
    
    # output the frame
    out.write(frame) 
    
    # The original input frame is shown in the window 
    cv2.imshow('Original', frame)

    # The window showing the operated video stream 
    cv2.imshow('frame', gray)

    
    # Wait for 'a' key to stop the program 
    if cv2.waitKey(1) & 0xFF == ord('a'):
        break
    
# Close the window / Release webcam
cap.release()
# After we release our webcam, we also release the out-out.release() 
# De-allocate any associated memory usage 
cv2.destroyAllWindows()