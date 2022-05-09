import cv2
import numpy as np


def my_function():
    img = cv2.VideoCapture("Resources/lambo.png")
    img.set(3, 600) #width
    img.set(4, 600) #height

    print(img.shape) ##(height, width, channels)

    imgResize = cv2.resize(img, (300, 200)) ##(width, height)

    cv2.imshow("Image", img)

    imgCropped = img[0:200, 200:500] ##[height1-height2, width1-width2]

    
    cv2.waitKey(0)


my_function()