import cv2
import numpy as np


def filter_mask(path):
    # Read in a map image
    img = cv2.imread(path)

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # define pink color range
    lower_bound = np.array([150, 90, 50])
    upper_bound = np.array([180, 255, 255])

    # Create a mask using the bounds set
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    #  Filter only pink from the original image using the mask
    res = cv2.bitwise_and(img, img, mask=mask)

    mask_inv = cv2.bitwise_not(mask)

    # Create resizable windows for the images
    # cv2.namedWindow("res", cv2.WINDOW_NORMAL)
    # cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
    # cv2.namedWindow("mask_inv", cv2.WINDOW_NORMAL)
    # Display the image
    # cv2.imshow("res", res)
    # cv2.imshow("mask", mask)
    # cv2.imshow("mask_inv", mask_inv)

    # cv2.waitKey(0)

    return mask

