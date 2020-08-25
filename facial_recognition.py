import argparse
import face_recognition
import json
import numpy as np
import os
from PIL import Image, ImageDraw


def load_image(path_to_img):
	image = face_recognition.load_image_file()
	return image
def get_face_locations(image):
	face_locations = face_recognition.face_locations(image)
	return face_locations
def compare_faces(list_of_training_imgs, img2):
	face1 = []
	for training_img in list_of_training_imgs:
		face1.append(face_recognition.face_encodings(training_img)[0])
	face2 = face_recognition.face_encodings(img2)[0]
	return face_recognition.compare_faces(face,face2, tolerance = 0.6)
def pull_faces(img):
	face_locations = get_face_locations(image)
	for face in face_locations:
		top, right, bottom left = face
		cropped = img[top:bottom, left:right]
		pil_img = Image.fromarray(cropped)
		pil_img.save(f'{top}.jpg')
def label_faces(img, known_encodings, known_names):
	face_locations = get_face_locations(img)
	face_encodings = face_recognition.face_encodings(img,face_locations)
	pil_img = Image.fromarray(img)
	draw = ImageDraw.Draw(pil_img)
	for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
		matches = face_recognition.compare_faces(known_encodings, face_encoding)
		name = "Unknown Person"
		if True in matches:
			match_index = matches.index(True)
			name = known_names[match_index]
		draw.rectangle(((left,top),(right,bottom)),outline = (0,0,0))
		text_width, text_height = draw.textsize(name)
		draw.rectangle(((left, bottom-textheight-10), (right, bottom)), fill=(0,0,0), outline = (0,0,0))
		draw.text((left+10, bottom - textheight - 5), name, fill = (255,255,255,255))
	del draw
def add_labels(list_of_img_files, list_of_labels, file_to_write = "./labels.json", overwrite = True):
	"""
	Creates (or writes to) JSON File in the format: {
	"labels":[]
	"encodings":[]
	}
	"""
	try:
		with open(file_to_write,'r') as f:
			data = json.loads(f.read())
	except IOError:
		data = {
		"labels":[]
		"encodings":[]
		}
		print("Existing file not found. Creating file "+file_to_write)
	for label, img_file in zip(list_of_labels, list_of_img_files):
		if label in data["labels"]:
			if overwrite:
				idx = data["labels"].index(label)
			else:
				data["labels"].append(label)
				data["encodings"].append(face_recognition.face_encodings(load_image(img_file)))
	with open(file_to_write, "wt") as fp:
		json.dump(data, fp)

def pull_labels(file = "./labels.json"):



