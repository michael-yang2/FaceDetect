import numpy as np
import cv2
import facial_recognition
def vid_capture(known_labels, known_encodings):
	cap = cv2.VideoCapture(0)
	cap.set(3,640) # set Width
	cap.set(4,480) # set Height
	while(True):
	    ret, frame = cap.read()
	    cv2.imshow('A', facial_recognition.label_faces(frame, known_encodings, known_labels))
	    k = cv2.waitKey(30) & 0xff
	    if k == 27: # press 'ESC' to quit
	        break
	cap.release()
	cv2.destroyAllWindows()
def run():
	labels, encodings = facial_recognition.pull_labels()
	vid_capture(labels, encodings)
run()