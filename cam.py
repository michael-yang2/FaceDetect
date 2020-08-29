import numpy as np
import cv2
import facial_recognition
cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height
while(True):
    ret, frame = cap.read()
    rgb_frame = frame[:, :, ::-1]

    
    cv2.imshow('frame', frame)
    cv2.imshow('gray', facial_recognition.label_faces(gray, [], [], ""))
    
    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break
cap.release()
cv2.destroyAllWindows()