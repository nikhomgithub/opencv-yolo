import cv2
import numpy as np 

img1=cv2.imread("images/road.jpg")
img2=cv2.imread("images/car.jpg")

img2_gray=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#create threashold to make pixel > 230 to be white(255)
ret,threshold=cv2.threshold(img2_gray,230,255,cv2.THRESH_BINARY)
cv2.imshow("threshold",threshold)
road=cv2.bitwise_and(img1,img1,mask=threshold)
cv2.imshow("road",road)

ret,mask=cv2.threshold(img2_gray,250,255,cv2.THRESH_BINARY_INV)
#mask made from car.jpg
cv2.imshow('mask',mask)

car=cv2.bitwise_and(img2,img2,mask=mask)
cv2.imshow("car",car)

combine=cv2.add(road,car)
cv2.imshow("combin",combine)

while True:
    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break
cv2.destroyAllWindows()