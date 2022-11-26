import cv2
import numpy as np
import matplotlib.pyplot as plt
import gpxpy
import gpxpy.gpx

path_map = '/Users/isoyang/PycharmProjects/oruns/maps/25052021.jpg'
path_gpx = '/Users/isoyang/PycharmProjects/oruns/maps/18052021.gpx'


def main():

    # Reads in a map image
    img = cv2.imread(path_map)
    print(img)

    # Extracts the pink color range on black background
    mask = filter_mask(img)

    # voiko kielletyn alueen filtteröidä pois maskista?? Tai tunnistaa rastiviivat ja hyödyntää niitä kiellettyjen
    # alueiden filtteröinnissä

    # Uses HoughCircles to detect route control points and their coordinates
    # Create better names for Hough parameters!!!
    control_circles = cv2.HoughCircles(mask,
                                        cv2.HOUGH_GRADIENT, 1, 20, param1=25,
                                        param2=16, minRadius=50, maxRadius=70)

    # Displays the detected control point to the user
    show_circles(control_circles, img)


def show_circles(circles, image):
    """
    :param circles: detected control coordinates
    :param image: desired background image/map for the circles
    :return: displays the detected controls
    """
    if circles is not None:

        # Convert the circle parameters a, b and r to integers.
        control_circles = np.uint16(np.around(circles))
        # print('output dimensions: ', circles.shape, '\n', circles)

        for pt in control_circles[0, :]:
            a, b, r = pt[0], pt[1], pt[2]

            # Draw the circumference of the circle.
            cv2.circle(image, (a, b), r, (255, 0, 0), 10)

            # Draw a small circle (of radius 1) to show the center.
            cv2.circle(image, (a, b), 1, (0, 0, 255), 5)
        plt.imshow(image)
        plt.show()
    else:
        print('No circles detected')


def filter_mask(img):
    """
    :param img: original map
    :return: returns a mask which highlights the pink color range used in orienteering maps for controls
    """

    # Convert image to HSV (hue, saturation, value) colorspace
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    print(hsv)

    # define pink color range
    lower_bound = np.array([150, 90, 50])
    upper_bound = np.array([180, 255, 255])

    # Create a mask using the bounds set
    mask = cv2.inRange(hsv, lower_bound, upper_bound)
    print(mask)
    #  Filter only pink from the original image using the mask
    res = cv2.bitwise_and(img, img, mask=mask)

    # Create resizable windows for the images
    # cv2.namedWindow("res", cv2.WINDOW_NORMAL)
    # cv2.namedWindow("mask", cv2.WINDOW_NORMAL)
    # cv2.namedWindow("mask_inv", cv2.WINDOW_NORMAL)
    # Display the image
    # cv2.imshow("res", res)
    cv2.imshow("mask", mask)
    # cv2.imshow("mask_inv", mask_inv)

    # cv2.waitKey(0)

    return mask

if __name__ == '__main__':
    main()

