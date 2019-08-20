import cv2
import numpy as np 

img=cv2.imread("images/red_panda.jpg")
print(img.shape)
rows,cols,ch=img.shape

#resize_img=cv2.resize(img,(400,500))
resize_img=cv2.resize(img,None,fx=0.5,fy=0.5)

matrixT=np.float32([[1,0,100],[0,1,50]])

tran_img=cv2.warpAffine(img,matrixT,(cols,rows))

matrixR=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
rot_img=cv2.warpAffine(img,matrixR,(cols,rows))

cv2.imshow("orig",img)
cv2.imshow("resize",resize_img)
cv2.imshow("tran",tran_img)
cv2.imshow("rotate",rot_img)
while True:
    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break
cv2.destroyAllWindows()
