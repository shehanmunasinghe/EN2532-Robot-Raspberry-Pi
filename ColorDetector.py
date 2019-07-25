from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

import numpy as np
import imutils
from collections import deque

class ColorDetector():
    def __init__(self):
        self.camera = PiCamera()
        self.RESOLUTION= (640,480) #(1024,768)#(640,480)
        self.camera.resolution=self.RESOLUTION
        self.rawCapture = PiRGBArray(self.camera,size=self.RESOLUTION)
        time.sleep(0.2)

        self.color_thresholds = {
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


    def getImage(self):
        self.camera.capture(self.rawCapture, format="bgr")
        self.image = self.rawCapture.array
        return self.image

    def detect_red(frame,hsv_frame):
        # Threshold the HSV image to get only blue colors
        mask_red1 = cv2.inRange(hsv_frame, self.color_thresholds['lower_red'], color_thresholds['upper_red'])
        mask_red2 = cv2.inRange(hsv_frame, self.color_thresholds['lower_pink'], color_thresholds['upper_pink'])
        mask_red = mask_red1 | mask_red2

        mask_red = cv2.erode(mask_red, None, iterations=2)
        mask_red = cv2.dilate(mask_red, None, iterations=2)

        #cv2.imshow('mask_red',mask_red)

        # Bitwise-AND mask and original image
        res_red = cv2.bitwise_and(frame,frame, mask= mask_red)
        cv2.imshow('res_red',res_red)

        return np.sum(res_red)

    def detect_blue(frame,hsv_frame):
        # Threshold the HSV image to get only blue colors
        mask_blue = cv2.inRange(hsv_frame, self.color_thresholds['lower_blue'], color_thresholds['upper_blue'])


        #mask_blue = cv2.erode(mask_blue, None, iterations=2)
        #mask_blue = cv2.dilate(mask_blue, None, iterations=2)

        #cv2.imshow('mask_blue',mask_blue)

        # Bitwise-AND mask and original image
        res_blue = cv2.bitwise_and(frame,frame, mask= mask_blue)

        cv2.imshow('res_blue',res_blue)

        return np.sum(res_blue)

    def detect_green(frame,hsv_frame):
        # Threshold the HSV image to get only green colors
        mask_green = cv2.inRange(hsv_frame, self.color_thresholds['lower_green'], color_thresholds['upper_green'])


        #mask_green = cv2.erode(mask_green, None, iterations=2)
        #mask_green = cv2.dilate(mask_green, None, iterations=2)

        #cv2.imshow('mask_green',mask_green)

        # Bitwise-AND mask and original image
        res_green = cv2.bitwise_and(frame,frame, mask= mask_green)

        cv2.imshow('res_green',res_green)

        return np.sum(res_green)
        
    def detect(self,frame):

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        red_score=self.detect_red(frame,hsv_frame)
        blue_score=self.detect_blue(frame,hsv_frame)
        green_score=self.detect_green(frame,hsv_frame)      

        print(red_score,blue_score,green_score)  









if __name__ == "__main__":
    colorDetector=ColorDetector()
    image=colorDetector.getImage()

    detected_color= colorDetector.detect(image)

    # cv2.imshow("Image", image)
    # cv2.waitKey(0)

