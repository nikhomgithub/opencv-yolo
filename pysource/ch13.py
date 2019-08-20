#This to transform perspective image to be top-view image
#https://www.youtube.com/watch?v=PtCQH93GucA&list=PL6Yc5OUgcoTmTGACTa__vnifNA744Cz-q&index=13
import cv2
import numpy as np 

cap=cv2.VideoCapture(0)

red=(0,0,255)

while True:
    _,frame=cap.read()

    cv2.circle(frame,(155,120),5,red,-1)
    cv2.circle(frame,(480,120),5,red,-1)
    cv2.circle(frame,(20,475),5,red,-1)
    cv2.circle(frame,(620,475),5,red,-1)

    pts1=np.float32([[155,120],[480,120],[20,475],[620,475]])
    pts2=np.float32([[0,0],[400,0],[0,600],[400,600]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)

    result=cv2.warpPerspective(frame,matrix,(400,600))

    cv2.imshow("frame",frame)
    cv2.imshow("Perspec tranf",result)

    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break
cap.release()
cv2.destroyAllWindows()
