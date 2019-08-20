#https://www.learnopencv.com/invisibility-cloak-using-color-detection-and-segmentation-with-opencv//


import cv2
import numpy as np 
import time


"""
#0 for default cam on com
cap=cv2.VideoCapture(0) 

# We give some time for the camera to warm-up!
time.sleep(1)

for i in range(10):
  print(i)  
  ret,background = cap.read()
"""

img=cv2.imread("../images/beach.png")

print(img.shape)
ch=img.shape[0]/2
cw=img.shape[1]/2
print(ch)
print(cw)

cv2.imshow('img_BGR',img);  
# converting from BGR to HSV color space
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

cv2.imshow('img_SHV',hsv);  

while True:
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

"""
colors=background[round(ch),round(cw)]
print(colors)
cv2.imshow('background',background);  

while True:
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
#vdo#out.release()
cv2.destroyAllWindows()
"""