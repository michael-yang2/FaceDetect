import argparse
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
def get_imgs_and_labels(file_path):
    labels = []
    imgs = []
    for name in os.listdir(file_path):
        curr_imgs = os.path.join(file_path, name)
        curr_label = hash(name)
        if os.path.isdir(curr_imgs):
            for img_file in os.listdir(curr_imgs):
                img = facial_recognition.load_image(os.path.join(curr_imgs, img_file))
                imgs.append(img)
                labels.append(curr_label)
    return (imgs, labels)
def run(file_path):
    imgs, labels = get_imgs_and_labels(file_path)
    recognizer = train(imgs, labels)
def main():
    global args
    parser = argparse.ArgumentParser(description='...')
    parser.add_argument("-f", "--file_path",
                    help="training data files",
                    type=str, default="./training_data")
    args = parser.parse_args()
    run(args.file_path)
if __name__ == "__main__":
    main()