import cv2
import numpy as np 

def nothing(x):
    pass

cap=cv2.VideoCapture(0)

cv2.namedWindow("Trackbars")

cv2.createTrackbar("L_H","Trackbars",0,179,nothing)
cv2.createTrackbar("L_S","Trackbars",0,255,nothing)
cv2.createTrackbar("L_V","Trackbars",0,255,nothing)
cv2.createTrackbar("U_H","Trackbars",179,179,nothing)
cv2.createTrackbar("U_S","Trackbars",255,255,nothing)
cv2.createTrackbar("U_V","Trackbars",255,255,nothing)


#red color
#lower_blue=np.array([50,75,0])
#upper_blue=np.array([180,170,255])



while True:
    _,frame=cap.read()
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("L_H","Trackbars")
    l_s=cv2.getTrackbarPos("L_S","Trackbars")
    l_v=cv2.getTrackbarPos("L_V","Trackbars")
    u_h=cv2.getTrackbarPos("U_H","Trackbars")
    u_s=cv2.getTrackbarPos("U_S","Trackbars")
    u_v=cv2.getTrackbarPos("U_V","Trackbars")

    print(l_h,l_s,l_v,u_h,u_s,u_v)

    lower_blue=np.array([l_h,l_s,l_v])
    upper_blue=np.array([u_h,u_s,u_v])
    mask=cv2.inRange(hsv,lower_blue,upper_blue)
    
    result=cv2.bitwise_and(frame,frame,mask=mask)

    print(frame[320,240])
    cv2.rectangle(frame, (310,230), (330,250), (0,255,0), 2)

    cv2.imshow('frame',frame) 
    cv2.imshow('result',result)
    #cv2.imshow('mask',mask)


    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break
cap.release()
cv2.destroyAllWindows()