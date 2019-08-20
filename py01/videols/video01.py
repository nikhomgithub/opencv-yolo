#This exercise to capture, draw, save file the vedio from camera

import cv2
import numpy as np 

#0 for default camera on comuter
cap=cv2.VideoCapture(0)    

#Prepare to save recorded video into a file
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('../videos/output.avi',fourcc,20.0,(640,480))

#define color & font
green = (0, 255, 0)
x=0;
y=0;
font = cv2.FONT_HERSHEY_SIMPLEX

#take a single frame from video
ret,frame=cap.read()  
print(frame.shape) # (480, 640, 3)
print("height: {} pixels".format(frame.shape[0]))#228
print("width: {} pixels".format(frame.shape[1]))#350
print("channels: {}".format(frame.shape[2]))#3

#center of frame
centerX=round(frame.shape[1]/2)
centerY=round(frame.shape[0]/2)
print(centerX)
print(centerY)

#all the time to run capture,draw,save video 
while True:
    ret,frame=cap.read()  
    
    #put text into frame
    cv2.putText(frame,'OpenCV',(centerX,centerY), font, 1,green,5,cv2.LINE_AA)

    #draw regtangle in green into frame
    cv2.rectangle(frame, (10, 10), (x, y), green,2)
    #increase retangel size
    x=x+1;
    y=y+1
    #gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    
    #write video into file
    out.write(frame)
    #cv2.imshow('Gray',gray)

    if(x==400):
        x=0
        y=0
    
    #To press "q" to exit the program
    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()