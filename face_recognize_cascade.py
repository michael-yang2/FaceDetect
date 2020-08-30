import cv2
import numpy as np
import os
import facial_recognition

cascPath = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
eyePath = cv2.data.haarcascades + 'haarcascade_eye.xml'
smilePath = cv2.data.haarcascades + 'haarcascade_smile.xml'
valid_images = [".jpg",".gif",".png",".jpeg",".JPG"]



def rgb2gray(rgb):
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return np.array(gray, dtype = 'uint8')
def train(imgs, labels, trainer_path = 'trainer/trainer.yml'):
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(cascPath)
    faceSamples = []
    if os.path.exists(trainer_path):
        recognizer.read(trainer_path)
    for image in imgs:
        x,y,w,h = detector.detectMultiScale(rgb2gray(image))[0]
        faceSamples.append(rgb2gray(image)[y:y+h,x:x+w])
    recognizer.train(np.array(faceSamples), np.array(labels))
    recognizer.save(trainer_path)
    return recognizer
def run():
    f = open('./labels/labels.txt', 'r') 
    labels = [int(s.strip()) for s in f.readlines()] 
    imgs = []
    for img_file in sorted(os.listdir('./training_data')):
        ext = os.path.splitext(img_file)[1]
        if ext.lower() not in valid_images:
            continue
        imgs.append(facial_recognition.load_image('./training_data/'+img_file))
    train(imgs, np.array(labels))
run()