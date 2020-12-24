"""
Basic Python OpenCV practice
"""

import numpy as np
import cv2 as cv

# img = cv.imread('photos/2.jpeg')

# cv.imshow('pic', img)
# cv.waitKey(0)


# capture = cv.VideoCapture('videos/3.mp4')

# while True:
#   isTrue, frame = capture.read()
#   cv.imshow('video', frame)
#   if cv.waitKey(20) & 0xFF==ord('d'):
#     break

# capture.release()
# cv.destroyAllWindows()


# def rescaleFrame(frame, scale=0.75):
#   width = int(frame.shape[1]*scale)
#   height = int(frame.shape[0]*scale)
  
#   dimensions = (width, height)

#   return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# img = cv.imread('photos/2.jpeg')
# cv.imshow('pic', img)

# rs = rescaleFrame(img)
# cv.imshow('pic2', rs)

# cv.waitKey(0)


# capture = cv.VideoCapture('videos/2.mp4')

# while True:
#   isTrue, frame = capture.read()
#   res = rescaleFrame(frame, 0.3)
#   # cv.imshow('video', frame)
#   # res = cv.resize(frame, (500,500))
#   cv.imshow('video', res)
#   if cv.waitKey(20) & 0xFF==ord('d'):
#     break

# capture.release()
# cv.destroyAllWindows()


# blank = np.zeros((500,500), dtype='uint8')
# cv.imshow('Blank', blank)

# cv.waitKey(0)


# blank = np.zeros((500,500), dtype='uint8')
# cv.imshow('Blank', blank)

# rect = cv.rectangle(blank, (1,1), (250,250), (255,225,0), thickness=2)
# cv.imshow('rectangle', rect)

# rectt = cv.rectangle(blank, (1,1), (250,250), (225,0,0), thickness=-1)
# cv.imshow('rectt', rectt)


# cir = cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (255, 0, 0), thickness=3)
# cv.imshow('circle', cir)

# lin = cv.line(blank, (0,0), (250,250), (255, 0, 0), 2)
# cv.imshow('line', lin)

# txt = cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_COMPLEX, 1.0, (225,0,0), 2)
# cv.imshow('texxt', txt);

# cv.waitKey(0)


# img = cv.imread('photos/1.jpeg')
# cv.imshow('img',img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray',gray)

# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

# canny = cv.Canny(img, 125, 175)
# cv.imshow('canny', canny)

# dialated = cv.dilate(img, (3,3), iterations=1)
# dialate = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('dilated', dialated)
# cv.imshow('dilated', dialate)

# canny = cv.Canny(img, 125, 175)
# cv.imshow('canny', canny)

# dialated = cv.dilate(canny, (3,3), iterations=1)
# cv.imshow('dilated', dialated)


# eroded = cv.erode(dialated, (3,3), iterations=1)
# cv.imshow('eroded', eroded)

# resized = cv.resize(img, (500,500))
# cv.imshow('resized', resized)

# res = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
# cv.imshow('res', res)

# cropped = img[50:500, 200:400]
# cv.imshow('cropped', cropped)

# cv.waitKey(0)


# def translate(img, x, y):
#   transMat = np.float32([[1,0,x],[0,1,y]])
#   dimensions = (img.shape[1], img.shape[0])
#   return cv.warpAffine(img, transMat, dimensions)

# def rotate(img, angle, rotPoint=None):
#   (height, width) =  img.shape[:2]

#   if rotPoint is None:
#     rotPoint = (width//2, height//2)

#   rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
#   dimensions = (width, height)

#   return cv.warpAffine(img, rotMat, dimensions)

# img = cv.imread('photos/1.jpeg')
# cv.imshow('original', img)

# # tr = translate(img, 100, -100)
# # cv.imshow("translated",tr)

# rt = rotate(img, 90)
# cv.imshow('rotated', rt)

# fp = cv.flip(img,0)
# cv.imshow('flliped', fp)

# fp = cv.flip(img,1)
# cv.imshow('fllipe', fp)

# fp = cv.flip(img,-1)
# cv.imshow('fllipd', fp)

# cv.waitKey(0)


# blank = np.zeros((500,500), dtype='uint8')
# cv.imshow('Blank', blank)

# img = cv.imread('photos/1.jpeg')
# cv.imshow('original', img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray', gray)

# canny = cv.Canny(img, 125, 175)
# cv.imshow('canny', canny)

# contours, hierachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

# cv.drawContours(blank, contours, -1, (0,0,255), 2)

# cv.waitKey(0)

