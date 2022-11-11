import cv2
import pathlib
import numpy as np
from tkinter import *


def obj_detection():
    
    recording_flag = False
    
    capture = cv2.VideoCapture(0)
    codec = cv2.VideoWriter_fourcc(*'XVID')
    
    classes = ["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car",
               "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person",
               "pottedplant", "sheep", "sofa", "train", "tvmonitor"]


    min_confidence = 0.2


    # image_path = 'Images/People_on_Street.jpg'
    prototxt_path = 'Models/MobileNetSSD_deploy.prototxt'
    model_path = 'Models/MobileNetSSD_deploy.caffemodel'

    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    np.random.seed(543210)

    net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

    cap = cv2.VideoCapture(0)

    # image = cv2.imread(image_path)

    while True:

        _, image = cap.read()
        
        ret, frame_temp = cap.read()

        height, width = image.shape[0], image.shape[1]
        blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.010, (300, 300), 110)

        net.setInput(blob)
        detected_objects = net.forward()

        for i in range(detected_objects.shape[2]):
            confidence = detected_objects[0][0][i][2]

            if confidence > min_confidence:
                class_index = int(detected_objects[0, 0, i, 1])

                upper_left_x = int(detected_objects[0, 0, i, 3] * width)
                upper_left_y = int(detected_objects[0, 0, i, 4] * height)
                lower_right_x = int(detected_objects[0, 0, i, 5] * width)
                lower_right_y = int(detected_objects[0, 0, i, 6] * height)

                prediction_text = f"{classes[class_index]}: {confidence:.2f}%"

                cv2.rectangle(image, (upper_left_x, upper_left_y), (lower_right_x, lower_right_y), colors[class_index],
                              3)
                cv2.putText(image, prediction_text, (upper_left_x, upper_left_y - 15
                if upper_left_y < 30 else upper_left_y + 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, colors[class_index], 2)

        cv2.imshow("Camera View", image)
        
        key=cv2.waitKey(1)
        if key%256 == 27:
            break
        elif key%256 == 32:
            if recording_flag == False:
                # we are transitioning from not recording to recording
                output = cv2.VideoWriter('CAPTURE.avi', codec, 30, (640, 480))
                recording_flag = True
            else:
                # transitioning from recording to not recording
                recording_flag = False
        
        output = cv2.VideoWriter('CAPTURE.avi', codec, 30, (640, 480))
    
        if recording_flag:
            output.write(frame_temp)
    
    capture.release()
    output.release()
    cv2.destroyAllWindows()
    
def face_recignition():
    cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
    
    clf = cv2.CascadeClassifier(str(cascade_path))
    
    cam = cv2.VideoCapture(0)
    
    while True:
        _, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = clf.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (30, 30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        
        for (x, y, width, height) in faces:
            cv2.rectangle(frame, (x, y), (x+width, y+height), (255, 255, 0), 2)
            
        cv2.imshow("Faces", frame)
        if cv2.waitKey(1) == ord("q"):
            break

    cam.release()
    cam.destroyAllWindows()


face_recignition()
            
