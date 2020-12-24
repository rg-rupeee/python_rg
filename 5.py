"""
Basic Face Recognition using Python OpenCV haarCascades practice
"""

import numpy as np
import cv2 as cv

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



capture = cv.VideoCapture('videos/2.mp4')

while True:
  isTrue, frame = capture.read()
  resframe = rescaleFrame(frame, 0.3)
  # fliped = cv.flip(resframe, 0)
  img = rotate(resframe, -90)
  # cv.imshow('video', rotated)

  gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
  cv.imshow('gray', gray)

  haar_cascade = cv.CascadeClassifier('haar_face.xml')

  faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

  # print(len(faces_rect))

  for(x, y, w, h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (225,0,0), thickness=3)
  cv.imshow('detected', img)



  if cv.waitKey(20) & 0xFF==ord('d'):
    break

capture.release()
cv.destroyAllWindows()