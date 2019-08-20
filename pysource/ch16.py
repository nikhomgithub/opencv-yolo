import numpy as np 
import cv2

img=cv2.imread("images/early_1800.jpg")
cv2.imshow("Original",img)

averaging=cv2.blur(img,(5,5))
cv2.imshow("averaging",averaging)

gaussian=cv2.GaussianBlur(img,(21,21),0)
cv2.imshow("gaussian",gaussian)

median=cv2.medianBlur(img,5)
cv2.imshow("median",median)

bilateral=cv2.bilateralFilter(img,5,75,75)
cv2.imshow("bilateral",bilateral)

while True:
    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break
cv2.destroyAllWindows()
