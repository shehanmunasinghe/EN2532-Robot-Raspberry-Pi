import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# define range of blue color in HSV
color_thresholds = {
    'lower_blue' : np.array([110,50,50]),
    'upper_blue' : np.array([130,255,255]),

    'lower_red' : np.array([  0,50,50]),
    'upper_red' : np.array([  15,255,255]),

    'lower_green' : np.array([ 50,50,50]),
    #'upper_green' : np.array([ 70,255,255])
    'upper_green' : np.array([ 100,255,255])
}

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # Threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv_frame, color_thresholds['lower_blue'], color_thresholds['upper_blue'])
    mask_red = cv2.inRange(hsv_frame, color_thresholds['lower_red'], color_thresholds['upper_red'])
    mask_green = cv2.inRange(hsv_frame, color_thresholds['lower_green'], color_thresholds['upper_green'])

    # Bitwise-AND mask and original image
    res_blue = cv2.bitwise_and(frame,frame, mask= mask_blue)
    res_red = cv2.bitwise_and(frame,frame, mask= mask_red)
    res_green = cv2.bitwise_and(frame,frame, mask= mask_green)

    cv2.imshow('frame',frame)
    #cv2.imshow('mask_blue',mask_blue)
    #cv2.imshow('mask_red',mask_red)
    #cv2.imshow('mask_green',mask_green)

    cv2.imshow('res_blue',res_blue)
    cv2.imshow('res_red',res_red)
    cv2.imshow('res_green',res_green)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()