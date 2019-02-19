#For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is
#[0,255]. Different softwares use different scales. So if you are comparing OpenCV #values with them, you need to normalize these ranges.

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    lower_green = np.array([50, 100, 100])
    upper_green = np.array([70, 255, 255])
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([40, 255, 255])
    lower_red = np.array([-10, 100, 100])
    upper_red = np.array([10, 255, 255])
    lower_magenta = np.array([140, 100, 100])
    upper_magenta = np.array([160, 255, 255])
    lower_cyan = np.array([80, 100, 100])
    upper_cyan = np.array([100, 255, 255])
    lower_maroon = np.array([-10, 100, 100])
    upper_maroon = np.array([10, 255, 255])
    lower_purp = np.array([140, 100, 100])
    upper_purp = np.array([160, 255, 255])

    # Threshold the HSV image to get only blue colors
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    yellow_mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    red_mask = cv2.inRange(hsv, lower_red, upper_red)
    magenta_mask = cv2.inRange(hsv, lower_magenta, upper_magenta)
    cyan_mask = cv2.inRange(hsv, lower_cyan, upper_cyan)
    maroon_mask = cv2.inRange(hsv, lower_maroon, upper_maroon)
    purple_mask = cv2.inRange(hsv, lower_purp, upper_purp)
    mask = blue_mask + green_mask + red_mask + yellow_mask + magenta_mask + cyan_mask + maroon_mask + purple_mask

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    #refer to this link about cv2.waitKey(1) & 0xFF
    #https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1
    k = cv2.waitKey(1) & 0xFF
    if k == 27 :  		
         break
  
cv2.destroyAllWindows()
