import pickle
import numpy as np
import cv2 as cv


###############
def rescaleFrame(frame, scale=0.75):
  width = int(frame.shape[1]*scale)
  height = int(frame.shape[0]*scale)
  dimensions = (width, height)
  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def translate(img, x, y):
  transMat = np.float32([[1,0,x],[0,1,y]])
  dimensions = (img.shape[1], img.shape[0])
  return cv.warpAffine(img, transMat, dimensions)


def rotate(img, angle, rotPoint=None):
  (height, width) =  img.shape[:2]
  if rotPoint is None:
    rotPoint = (width//2, height//2)
  rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
  dimensions = (width, height)
  return cv.warpAffine(img, rotMat, dimensions)
###############


face_cascade = cv.CascadeClassifier('haar_face.xml')

recognizer = cv.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("labels.pickle", "rb") as f:
  og_labels = pickle.load(f)
  labels = {v:k for k,v in og_labels.items()}

capture = cv.VideoCapture('videos/2.mp4')


while True:
  isTrue, frame = capture.read()

  #########
  resframe = rescaleFrame(frame, 0.3)
  img = rotate(resframe, -90)
  #########
  
  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  # cv.imshow('gray', gray)


  faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=5)


  for(x, y, w, h) in faces:

    roi_gray = gray[y:y+h, x:x+w] #(ycord_start, ycord_end)
    roi_color = frame[y:y+h, x:x+w]

    # recognize?????????????????
    id_, conf = recognizer.predict(roi_gray)
    
    if(conf>45 and conf<100):
      print(labels[id_], conf)
    
      font = cv.FONT_HERSHEY_SIMPLEX
      name = labels[id_]
      color = (255, 0, 0)
      stroke = 2
      cv.putText(img, name, (x,y), font, 1, color, stroke, cv.LINE_AA)


    color = (255,0,0)
    stroke = 2
    end_cord_x = x+w
    end_cord_y = y+h
    cv.rectangle(img, (x,y), (end_cord_x,end_cord_y), color, stroke)
  cv.imshow('detected', img)



  if cv.waitKey(20) & 0xFF==ord('d'):
    break


capture.release()
cv.destroyAllWindows()