#https://www.youtube.com/watch?v=CCOXg75HkvM
# To detect red color in image 

import cv2
import numpy as np

lower_red=np.array([2,0,0])
upper_red=np.array([150,255,255])


#Change .png to be numpy array
img=cv2.imread("../images/beach.png")
#to see image i BGR format
cv2.imshow('img_BGR',img); 

#to check shape of numpy array
print(img.shape)
centerX=round(img.shape[1]/2)
centerY=round(img.shape[0]/2)
red = (0,0, 255)


imgSun=cv2.circle(img, (centerX, centerY), 20, red,-1)
#to see image i BGR format
cv2.imshow('imgSun_BGR',imgSun);  


#to convert BGR to HSV for color filter
hsv=cv2.cvtColor(imgSun,cv2.COLOR_BGR2HSV)
cv2.imshow('hsv',hsv)

mask=cv2.inRange(hsv,lower_red,upper_red)
cv2.imshow('mask',mask)

res=cv2.bitwise_and(imgSun,imgSun,mask=mask)
cv2.imshow('res',res)

while True:
    if cv2.waitKey(1)&0xFF==ord('q'):
        break
cv2.destroyAllWindows()
