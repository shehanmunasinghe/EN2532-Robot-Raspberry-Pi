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

def detect_circles(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply hough transform on the image
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, minDist=100, param1=200, param2=10, minRadius=60, maxRadius=int(150))
    # Draw detected circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw outer circle
            cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw inner circle
            cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
    return img
    
def detect_circles2(mask_blue,res_blue):
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply hough transform on the image
    circles = cv2.HoughCircles(mask_blue, cv2.HOUGH_GRADIENT, 1, minDist=100, param1=200, param2=10, minRadius=60, maxRadius=int(150))
    # Draw detected circles
    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            # Draw outer circle
            cv2.circle(res_blue, (i[0], i[1]), i[2], (0, 255, 0), 2)
            # Draw inner circle
            cv2.circle(res_blue, (i[0], i[1]), 2, (0, 0, 255), 3)
    return res_blue
 

while(1):

    # Take each frame
    _, frame = cap.read()

    # Noise Filter
    #frame = cv2.medianBlur(frame,5)
    #frame = cv2.GaussianBlur(frame,(5,5),0)

    # Convert BGR to HSV
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    # Threshold the HSV image to get only blue colors
    mask_blue = cv2.inRange(hsv_frame, color_thresholds['lower_blue'], color_thresholds['upper_blue'])
    mask_blue = cv2.erode(mask_blue, None, iterations=2)
    mask_blue = cv2.dilate(mask_blue, None, iterations=2)
    # Bitwise-AND mask and original image
    res_blue = cv2.bitwise_and(frame,frame, mask= mask_blue)


    cv2.imshow('frame',frame)
    cv2.imshow('mask_blue',mask_blue)

    detected = detect_circles2(mask_blue,res_blue)
    cv2.imshow('res_blue',detected)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()