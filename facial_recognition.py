import face_recognition
from PIL import image


def load_image(path_to_img):
	image = face_recognition.load_image_file()
	return image
def get_face_locations(image):
	face_locations = face_recognition.face_locations(image)
	return face_locations

def compare_faces(list_of_training_imgs, img2):
	face1 = []
	for traning_img in list_of_training_imgs:
		face1.append(face_recognition.face_encodings(training_img)[0])
	face2 = face_recognition.face_encodings(img2)[0]
	return face_recognition.compare_faces(face,face2, tolerance = 0.6)