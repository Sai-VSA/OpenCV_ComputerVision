import cv2
from cv2 import getTrackbarPos
import numpy as np


def empty(i):
    pass

def my_function():
    cv2.namedWindow('TrackBars')
    cv2.resizeWindow('TrackBars', 640, 240)

    cv2.createTrackbar('Hue Min', "TrackBars", 0, 179, empty) 
    cv2.createTrackbar('Hue Max', "TrackBars", 179, 179, empty) 
    cv2.createTrackbar('Saturation Min', "TrackBars", 0, 255, empty) 
    cv2.createTrackbar('Saturation Max', "TrackBars", 255, 255, empty) 
    cv2.createTrackbar('Value Min', "TrackBars", 0, 255, empty) 
    cv2.createTrackbar('Value Max', "TrackBars", 255, 255, empty) 
    #(value changed, window assined to, initial hue val, n out of 179 hue, function to run when trackbar changes)
    #HSV values can be set to necessary colour values after testing with mask and trackbar

    while 1:
        img = cv2.imread("Resources/Sample.png")
        imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        h_min = getTrackbarPos('Hue Min', 'TrackBars')
        h_max = getTrackbarPos('Hue Max', 'TrackBars')
        s_min = getTrackbarPos('Saturation Min', 'TrackBars ')
        s_max = getTrackbarPos('Saturation Max', 'TrackBars')
        v_min = getTrackbarPos('Value Min', 'TrackBars')
        v_max = getTrackbarPos('Value Max', 'TrackBars')


        print(h_min, h_max, s_min, s_max, v_min, v_max) ##values can be used to filter out colour in that range

        #lower = np.zeros((img.shape[1], img.shape[2]))
        #lower[:] = (h_min, s_min, v_min)

        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])


        mask = cv2.inRange(imgHSV, lower, upper)

        imgResult = cv2.bitwise_and(img, img, mask = mask) #uses mask on image and gets fitting values from image to makew new picture



        cv2.imshow('Original', img)
        cv2.imshow('HSV', imgHSV)
        cv2.waitKey(1)


my_function()