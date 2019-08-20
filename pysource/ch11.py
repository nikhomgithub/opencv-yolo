import cv2 
import numpy as np
from matplotlib import pyplot as plt

"""
img=np.zeros((100,100),np.uint8)

cv2.rectangle(img,(0,50),(100,100),(255),-1)
cv2.circle(img,(50,50),25,(127),-1)
cv2.imshow("img",img)

plt.hist(img.ravel(),256,[0,256])
plt.show()
"""

"""
image=cv2.imread("images/sea_beach.jpg",cv2.IMREAD_GRAYSCALE)
print(image.shape)
cv2.imshow("sea beach",image)

plt.hist(image.ravel(),256,[0,256])
plt.show()
"""

img_sea=cv2.imread("images/sea_beach.jpg")

b,g,r=cv2.split(img_sea)

cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)


plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])


plt.show()




while True:
    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break
cv2.destroyAllWindows()
