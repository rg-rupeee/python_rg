"""
Basic Face Detection using Python OpenCV haarCascades practice
"""

import cv2 as cv
import numpy as np

def rescaleFrame(frame, scale=0.75):
  width = int(frame.shape[1]*scale)
  height = int(frame.shape[0]*scale)
  
  dimensions = (width, height)

  return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

img = cv.imread('photos/g2.jpg')
img = rescaleFrame(img,0.1)
cv.imshow('pic', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(len(faces_rect))

for(x, y, w, h) in faces_rect:
  cv.rectangle(img, (x,y), (x+w,y+h), (225,0,0), thickness=3)
cv.imshow('detected', img)

cv.waitKey(0)