import cv2
import numpy as np
import imutils
from collections import deque

import time

#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('http://shehan:shehan@192.168.1.104:8080/video')
cap = cv2.VideoCapture('http://192.168.1.103:8080/video')


# define range of blue color in HSV
color_thresholds = {
    'lower_blue' : np.array([110,50,50]),
    'upper_blue' : np.array([130,255,255]),

    'lower_red' : np.array([  0,50,50]),
    'upper_red' : np.array([  15,255,255]),
    'lower_pink' : np.array([  170,100,100]),
    'upper_pink' : np.array([  180,255,255]),

    'lower_green' : np.array([ 50,50,50]),
    #'upper_green' : np.array([ 70,255,255])
    'upper_green' : np.array([ 100,255,255])
}
   
def is_true_circle(circle, mask,res):
    x,y,r = circle[0], circle[1], circle[2]
    if x-r<0 or y-r<0 or x+r>mask.shape[1] or y+r>mask.shape[0]:
        return False
    else:
        #roi=mask.copy()[x-r:x+r , y-r:y+r]
        roi=mask.copy()[y-r:y+r , x-r:x+r]

        #score=np.sum(roi)/(roi.shape[0]*roi.shape[1])
        score=np.sum(roi)/(np.pi*r*r)/255

        if  (score!=np.nan and score>0.5) :
            cv2.rectangle(res,(x-r,y-r),(x+r,y+r),(0,255,0),3)
            #cv2.putText(res,str(score),(x+r,y+r), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
            cv2.putText(res,str(roi.shape),(x+r,y+r), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
            cv2.putText(res,str(score),(x+r,y+r+20), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
            
            try:
                cv2.imshow('roi',roi)
            except:
                print("error1")
                
            return True
        else:
            return False

def detect_circles2(mask,res):
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply hough transform on the image
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, minDist=200, param1=200, param2=10, minRadius=60, maxRadius=int(150))
    # Draw detected circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            if is_true_circle(circle,mask,res):
                # Draw outer circle
                cv2.circle(res, (circle[0], circle[1]), circle[2], (0, 255, 0), 2)
                # Draw inner circle
                cv2.circle(res, (circle[0], circle[1]), 2, (0, 0, 255), 3)
    return res

def get_circle_score(x,y,r, mask):
    if x-r<0 or y-r<0 or x+r>mask.shape[1] or y+r>mask.shape[0]:
        return False
    else:
        #roi=mask.copy()[x-r:x+r , y-r:y+r]
        roi=mask.copy()[y-r:y+r , x-r:x+r]

        #score=np.sum(roi)/(roi.shape[0]*roi.shape[1])
        score=np.sum(roi)/(np.pi*r*r)/255

        return score

def detect_circles4(mask,res):
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    max_score=0
    # Apply hough transform on the image
    circles = cv2.HoughCircles(mask, cv2.HOUGH_GRADIENT, 1, minDist=70, param1=200, param2=10, minRadius=60, maxRadius=int(150))
    # Draw detected circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for circle in circles[0, :]:
            x,y,r = circle[0], circle[1], circle[2]
            circle_score=get_circle_score(x,y,r,mask)
            if (circle_score!=np.nan and circle_score>0.7) :
                if circle_score>max_score : max_score=circle_score
                # Draw outer circle
                cv2.circle(res, (x, y), r, (0, 255, 0), 2)
                # Draw inner circle
                cv2.circle(res, (x, y), 2, (0, 0, 255), 3)

                cv2.rectangle(res,(x-r,y-r),(x+r,y+r),(0,255,0),3)
                cv2.putText(res,str(circle_score),(x+r,y+r+20), cv2.FONT_HERSHEY_SIMPLEX, 1,(255,255,255),2,cv2.LINE_AA)
                
    return max_score,res

def detect_red(frame,hsv_frame):
    # Threshold the HSV image to get only blue colors
    mask_red1 = cv2.inRange(hsv_frame, color_thresholds['lower_red'], color_thresholds['upper_red'])
    mask_red2 = cv2.inRange(hsv_frame, color_thresholds['lower_pink'], color_thresholds['upper_pink'])
    mask_red = mask_red1 | mask_red2

    mask_red = cv2.erode(mask_red, None, iterations=2)
    mask_red = cv2.dilate(mask_red, None, iterations=2)

    #cv2.imshow('mask_red',mask_red)

    # Bitwise-AND mask and original image
    res_red = cv2.bitwise_and(frame,frame, mask= mask_red)

    #detected = detect_circles2(mask_red,res_red)
    max_score,detected = detect_circles4(mask_red,res_red)
    cv2.imshow('res_red',detected)

    return max_score

def detect_blue(frame,hsv_frame):
    # Threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv_frame, color_thresholds['lower_blue'], color_thresholds['upper_blue'])


    #mask_blue = cv2.erode(mask_blue, None, iterations=2)
    #mask_blue = cv2.dilate(mask_blue, None, iterations=2)

    #cv2.imshow('mask_blue',mask_blue)

    # Bitwise-AND mask and original image
    res_blue = cv2.bitwise_and(frame,frame, mask= mask_blue)

    #detected = detect_circles2(mask_blue,res_blue)
    max_score,detected = detect_circles4(mask_blue,res_blue)
    cv2.imshow('res_blue',detected)

    return max_score

def detect_green(frame,hsv_frame):
    # Threshold the HSV image to get only green colors
    mask_green = cv2.inRange(hsv_frame, color_thresholds['lower_green'], color_thresholds['upper_green'])


    #mask_green = cv2.erode(mask_green, None, iterations=2)
    #mask_green = cv2.dilate(mask_green, None, iterations=2)

    #cv2.imshow('mask_green',mask_green)

    # Bitwise-AND mask and original image
    res_green = cv2.bitwise_and(frame,frame, mask= mask_green)

    #detected = detect_circles2(mask_green,res_green)
    max_score,detected = detect_circles4(mask_green,res_green)
    cv2.imshow('res_green',detected)

    return max_score


while(1):

    # Take each frame
    _, frame = cap.read()

    # Noise Filter
    #frame = cv2.medianBlur(frame,5)
    #frame = cv2.GaussianBlur(frame,(5,5),0)

    # Convert BGR to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_score=detect_red(frame,hsv_frame)
    blue_score=detect_blue(frame,hsv_frame)
    green_score=detect_green(frame,hsv_frame)


    cv2.imshow('frame',frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

    #time.sleep(0.5)

cv2.destroyAllWindows()