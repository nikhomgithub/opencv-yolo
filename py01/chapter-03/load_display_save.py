# USAGE
# python load_display_save.py --image ../images/trex.png

# Import the necessary packages
from __future__ import print_function
import argparse
import cv2 as cv2
import numpy as np
#~/pythonhome/py01/chapter-03$ python load_display_save.py --image ../images/trex.png
# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,help = "Path to the image")
args = vars(ap.parse_args())
#print(args)

# Load the image and show some basic information on it
image = cv2.imread(args["image"])
print(image.shape)
#228,350,3

print("height: {} pixels".format(image.shape[0]))#228
print("width: {} pixels".format(image.shape[1]))#350
print("channels: {}".format(image.shape[2]))#3

#print(image)

# Show the image and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(7000)

# Save the image -- OpenCV handles converting filetypes
# automatically
#cv2.imwrite("newimage.jpg", image)
