import numpy as np
import cv2 as cv
import random

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
movementx = 10
movementy = -10
alpha = 0.7
chance=0.3
ypad = 50
xpad = 30
def processit(frame,whole_frame=False,randomzoom=False):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        # Padding if needed
        x = x-xpad
        y = y-ypad
        w=w+xpad
        h=h+2*ypad
        roi_color = frame[y:y+h, x:x+w]

        if whole_frame:
            roi_color = frame
        M = np.float32([[1,0,movementx],[0,1,movementy]])

        # Grab each channel
        red = roi_color.copy()
        red[:, :, 1] = 0
        red[:, :, 2] = 0
        red_shifted = cv2.warpAffine(red,M,(roi_color.shape[1],roi_color.shape[0])) # we get shifted image

        blue = roi_color.copy()
        blue[:, :, 1] = 0
        blue[:, :, 0] = 0
        blue_shifted = cv2.warpAffine(blue,M,(roi_color.shape[1],roi_color.shape[0])) # we get shifted image

        green = roi_color.copy()
        green[:, :, 2] = 0
        green[:, :, 0] = 0
        green_shifted = cv2.warpAffine(green,M,(roi_color.shape[1],roi_color.shape[0])) # we get shifted image

        #randomly set the channels to zero so it has no effect
        if random.random()<=chance:
            red_shifted = 0

        if random.random()<=chance:
            blue_shifted = 0

        if random.random()<=chance:
            green_shifted = 0

        #Add them all back
        shifted = red_shifted + blue_shifted + green_shifted

        roi_color = cv2.addWeighted(roi_color, alpha, shifted, 1-alpha, 0)

        y1,y2=y,y+roi_color.shape[0]
        x1,x2=x,x+roi_color.shape[1]
        if whole_frame:
            frame = roi_color
        else:
            frame[y1:y2,x1:x2]=roi_color
        if randomzoom and random.random()<0.8:
            frame = cv2.resize(roi_color,(640,480))
            process_this_frame=False

    return frame


lastframe= None
count = 0
while(True):
    # Capture frame-by-frame
    try:
        ret, frame = cap.read()
        lastframe = processit(frame)
        cv2.imshow('frame',lastframe)
    except:
        cv2.imshow('frame',lastframe)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break   