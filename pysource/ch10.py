import cv2
import numpy as np 

img=cv2.imread('images/black_to_white.jpeg',cv2.IMREAD_GRAYSCALE)

ret,threshold_binary=cv2.threshold(img,128,255,cv2.THRESH_BINARY)
ret,threshold_binary_inv=cv2.threshold(img,128,255,cv2.THRESH_BINARY_INV)
ret,threshold_trunc=cv2.threshold(img,128,255,cv2.THRESH_TRUNC)
ret,threshold_tozero=cv2.threshold(img,128,255,cv2.THRESH_TOZERO)



cv2.imshow("img",img)
cv2.imshow("binary",threshold_binary);
cv2.imshow("binary_inv",threshold_binary_inv);
cv2.imshow("trunc",threshold_trunc);
cv2.imshow("tozero",threshold_tozero);


while True:
    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break
cv2.destroyAllWindows()
