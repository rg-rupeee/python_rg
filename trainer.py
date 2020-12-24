import os
import pickle
from PIL import Image
import numpy as np
import cv2


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

image_dir = os.path.join(BASE_DIR, "images")

face_cascade = cv2.CascadeClassifier('haar_face.xml')

current_id = 0
labels_ids = {}
y_labels = []
x_train = []

for root, dirs, files in os.walk(image_dir):
  for file in files:
    if file.endswith('png') or file.endswith('jpg') or file.endswith('jpeg'):
      path = os.path.join(root, file)
      label = os.path.basename(root).replace(" ", "-").lower()
      print(label, path)

      if not label in labels_ids:
        labels_ids[label] = current_id
        current_id+=1

      id_ = labels_ids[label]
      print(labels_ids)

      pil_image = Image.open(path).convert("L")
      
      image_array = np.array(pil_image, "uint8")
      print(image_array)

      faces = face_cascade.detectMultiScale(image_array, scaleFactor=1.2, minNeighbors=3)

      for(x,y,w,h) in faces:
        roi = image_array[y:y+h, x:x+w]
        x_train.append(roi)
        y_labels.append(id_)

print(y_labels)
print(x_train)

with open("labels.pickle", "wb") as f:
  pickle.dump(labels_ids,f)

recognizer = cv2.face.LBPHFaceRecognizer_create()


recognizer.train(x_train,np.array(y_labels))

recognizer.save('trainner.yml')