#basic cap image from camera 
#save as video in avi format

import cv2
import numpy as np 

#0 for default cam on com
cap=cv2.VideoCapture(0)    
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('../videos/output00.avi',fourcc,20.0,(640,480))

while True:
    ret,frame=cap.read()  

    cv2.imshow('frame',frame)
    out.write(frame)
    
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()