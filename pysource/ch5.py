import cv2
import numpy as np 

imgChev=cv2.imread("images/chev.jpg")
cv2.imshow("Original",imgChev)

sum=cv2.add(imgChev,imgChev)
cv2.imshow("sum",sum)

sum_weighted=cv2.addWeighted(imgChev,0.3,imgChev,0.3,0)
cv2.imshow("sum weighted",sum_weighted)

imgChev_gray=cv2.cvtColor(imgChev,cv2.COLOR_BGR2GRAY)

ret,threshold=cv2.threshold(imgChev_gray,240,255,cv2.THRESH_BINARY) 
#change color from 0-240 to be 255
cv2.imshow("threshold",threshold)

ret,mask=cv2.threshold(imgChev_gray,240,255,cv2.THRESH_BINARY_INV) 
cv2.imshow("mask",mask)

sum_mask=cv2.add(imgChev,imgChev,mask=mask)
cv2.imshow("sum_mask",sum_mask)



while True:
    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break
cv2.destroyAllWindows()
