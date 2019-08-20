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
image = cv2.imread(args["image"],cv2.IMREAD_GRAYSCALE)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,'OpenCV',(50,50), font, 1,(0,255,0),5,cv2.LINE_AA)


cv2.imshow("Gray",image)
cv2.imwrite('gray.png',image)


cv2.waitKey(7000)