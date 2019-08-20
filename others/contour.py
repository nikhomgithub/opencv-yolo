import cv2
import numpy as np 

img_logo=cv2.imread("../pysource/images/logo.png")

logo_gray=cv2.cvtColor(img_logo,cv2.COLOR_BGR2GRAY)

ret,threshold=cv2.threshold(logo_gray,200,255,0)
cv2.imshow("threshold",threshold)

contours,hierarchy = cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

print(contours[0])

cv2.drawContours(img_logo,contours,-1,(0,255,0),2)
#-1 mean all

cv2.imshow("logo",img_logo)

while True:
    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break
cv2.destroyAllWindows()