import cv2
import numpy as np


def my_function():
    img = cv2.imread("Resources/test_img")

    width = img.shape[0]
    height = img.shape[1]

    pts1 = np.float([[111, 219], [287, 188], [154, 482], [352, 440]]) #
    pts2 = np.float([[0,0], [width, 0], [0, height], [width, height]])

    matrix = cv2.getPerspectiveTransform(pts1, pts2) #selects an area between pt1 and shifts it to fit pt2 matrix
    imgOutput = cv2.warpPerspective(img, matrix, (width, height))


    cv2.imshow("Image", img)
    cv2.imshow("Image Output", imgOutput)
    


my_function()