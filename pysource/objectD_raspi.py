import cv2 
import numpy as np

def nothing(x):
    pass

cap=cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")

cv2.createTrackbar("L_H","Trackbars",76,179,nothing)
cv2.createTrackbar("L_S","Trackbars",134,255,nothing)
cv2.createTrackbar("L_V","Trackbars",119,255,nothing)
cv2.createTrackbar("U_H","Trackbars",179,179,nothing)
cv2.createTrackbar("U_S","Trackbars",255,255,nothing)
cv2.createTrackbar("U_V","Trackbars",255,255,nothing)


while True:
    _,frame=cap.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("L_H","Trackbars")
    l_s=cv2.getTrackbarPos("L_S","Trackbars")
    l_v=cv2.getTrackbarPos("L_V","Trackbars")
    u_h=cv2.getTrackbarPos("U_H","Trackbars")
    u_s=cv2.getTrackbarPos("U_S","Trackbars")
    u_v=cv2.getTrackbarPos("U_V","Trackbars")

    #print(l_h,l_s,l_v,u_h,u_s,u_v)

    lower_blue=np.array([l_h,l_s,l_v])
    upper_blue=np.array([u_h,u_s,u_v])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)

    _,contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours, key=lamba x:cv2.contourArea(x), reverse=True)

    for cnt in contours:
            (x,y,w,h)=cv2.boundingRect(cnt)

            x_medium=int((x+x+w)/2) 

    result=cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('result',result)

    key=cv2.waitKey(1)

    if key==27: #27 is ESC
        break

cap.release()
cv2.destroyAllWindows()