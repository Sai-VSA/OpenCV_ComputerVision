import cv2
import numpy as np


def my_function():
    img = np.zeros((512,512,3), np.uint8) ##define matrix size (width, height), colourscale 
    print(img) #prints the matrix
    print(img.shape) #prints image dimensions matrix
    #img[:] = (255,0, 0) #sets image colour in given range [y1:y2, x1:x2] 


    cv2.line(img, (0,0), (300,300), (255,0,0), 3) ##(image, start point (width, height), end point, colour, thickness)
    cv2.rectangle(img, (0,0), (250, 350), (0, 255, 0), cv2.FILLED) #cv2.FILLED fills rectangle 
    cv2.circle(img, (450, 50), 30, (255, 255, 0), 5) ##(image, center, radius, colour, thickness)
    cv2.putText(img, 'Text', (0, 0), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 120, 120), 1) #(image, text on image, Bottom Left of Text, font, font scaling, colour, thickness)


    cv2.imshow("Image", img)
    
    cv2.waitKey(0)


my_function()