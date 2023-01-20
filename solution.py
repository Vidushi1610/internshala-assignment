# importing libraries
import cv2
import numpy as np
import imutils

# Create a VideoCapture object and read from input file
capture = cv2.VideoCapture('AI.mp4')

# Read until video is completed
while(True):
	
# Capture frame-by-frame
    ret, frame = capture.read()
    frame = imutils.resize(frame, width=600)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1)  == ord('v'):
        break

