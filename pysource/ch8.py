import cv2
import numpy as np 

def nothing(x):
    pass

import cv2
import numpy as np 

cv2.namedWindow("frame")
#create a window named "frame"

cv2.createTrackbar("test","frame",50,500,nothing)
#creaate a trackbar name "test" inside window "a=name"

cv2.createTrackbar("color/gray","frame",0,1,nothing)

font=cv2.FONT_HERSHEY_COMPLEX
cap=cv2.VideoCapture(0)
while True:

    _,frame=cap.read()
    
    test=cv2.getTrackbarPos("test","frame")
    #get number from tracbar postion

    s=cv2.getTrackbarPos("color/gray","frame")
    #get number from tracbar postion
    
    cv2.putText(frame,str(test),(50,150),font,4,(0,0,255))
    #put text from str(test) 

    if(s==0):
        pass
    else:    
        frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)

    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break
cap.release()
cv2.destroyAllWindows()