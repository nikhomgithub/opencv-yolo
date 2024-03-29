import cv2
import numpy as np 

img1=cv2.imread('images/drawing_1.png')
img2=cv2.imread('images/drawing_2.png')

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)


bit_and=cv2.bitwise_and(img1,img2)
cv2.imshow('bit_and',bit_and)

bit_or=cv2.bitwise_or(img1,img2)
cv2.imshow('bit_or',bit_or)

bit_xor=cv2.bitwise_xor(img1,img2)
cv2.imshow('bit_xor',bit_xor)

bit_not=cv2.bitwise_not(img1)
cv2.imshow('bit_not',bit_not)

while True:
    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break
cv2.destroyAllWindows()