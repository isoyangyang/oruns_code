import cv2
import numpy as np
from matplotlib import pyplot as plt


path = '/Users/isoyang/PycharmProjects/oruns/testi1.jpg'


img = cv2.imread(path, -1)
cv2.imshow('map', img)

color = ('b', 'g', 'r')
for channel, col in enumerate(color):
    histr = cv2.calcHist([img], [channel], None, [256], [0, 256])
    plt.plot(histr, color=col)
    plt.xlim([0, 256])
plt.title('Histogram for color scale picture')
plt.show()