import cv2
import numpy as np
import os

cascPath = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
eyePath = cv2.data.haarcascades + 'haarcascade_eye.xml'
smilePath = cv2.data.haarcascades + 'haarcascade_smile.xml'

def detect_faces_cam():
    faceCascade = cv2.CascadeClassifier(cascPath)
    eyeCascade = cv2.CascadeClassifier(eyePath)
    smileCascade = cv2.CascadeClassifier(smilePath)

    font = cv2.FONT_HERSHEY_SIMPLEX
    video_capture = cv2.VideoCapture(0)
    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(200, 200),
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            cv2.putText(frame,'Face',(x, y), font, 2,(255,0,0),5)

        cv2.putText(frame,'Number of Faces : ' + str(len(faces)),(40, 40), font, 1,(255,0,0),2)      
        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    video_capture.release()
    cv2.destroyAllWindows()
def make_recognizer(file):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    if os.path.exists(file):
        recognizer.read(file)
    return recognizer
