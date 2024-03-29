import cv2
import imutils

from playsound import playsound

import threading
from playsound import playsound

from rich import box
from rich import print
from rich.panel import Panel

def beep():
    playsound("beep.wav")

def beep():
    playsound("beep.wav")

def alarm_bleep():
    global alarm
    for _ in range(5):
        if not alarm_mode:
            break
        print(Panel.fit("[b]ALARM !!", title = "[b]ALERT 🟥", title_align = "left", box = box.SQUARE, border_style = "bold red"))
        # New code
        beep()
    alarm = False


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

_, start_frame = cap.read()
start_frame = cv2.cvtColor(start_frame, cv2.COLOR_BGR2GRAY)
start_frame = cv2.GaussianBlur(start_frame, (21, 21), 0)

alarm = False
alarm_mode = False
alarm_counter = 0

    
while True:
    _, frame = cap.read()
    
    if alarm_mode:
        frame_bw = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_bw = cv2.GaussianBlur(frame_bw, (5, 5), 0)
        
        difference = cv2.absdiff(frame_bw, start_frame)
        threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
        start_frame = frame_bw
        
        if threshold.sum() > 300:
            alarm_counter += 1
        else:
            if alarm_counter > 0:
                alarm_counter -= 1
                
        cv2.imshow("Camera", threshold)
    else:
        cv2.imshow("Camera", frame)
        
    if alarm_counter > 20:
        if not alarm:
            alarm = True
            threading.Thread(target = alarm_bleep).start()
            
    key_pressed = cv2.waitKey(30)
    
    
    if key_pressed == ord("t"):
        alarm_mode = not alarm_mode
        alarm_counter = 0
    if key_pressed == ord("q"):
        alarm_mode = False
        break
    
    key = cv2.waitKey(1)
    if key == 27:
            break
    
    
cap.release()
cv2.destroyAllWindows()
