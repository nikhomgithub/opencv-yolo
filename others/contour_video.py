import cv2
import numpy as np 
import time

def nothing(x):
    pass

font=cv2.FONT_HERSHEY_COMPLEX

cv2.namedWindow("Trackbars")

cv2.createTrackbar("L_H","Trackbars",0,179,nothing)
cv2.createTrackbar("L_S","Trackbars",189,255,nothing)
cv2.createTrackbar("L_V","Trackbars",247,255,nothing)
cv2.createTrackbar("U_H","Trackbars",11,179,nothing)
cv2.createTrackbar("U_S","Trackbars",255,255,nothing)
cv2.createTrackbar("U_V","Trackbars",255,255,nothing)

# Initialize our canvas as a 300x300 with 3 channels,
# Red, Green, and Blue, with a black background
count=0
cx=100
cy=100

while True:
    #frame=cv2.imread("../pysource/images/logo.png")
    #cv2.imshow("frame",frame)
    frame = np.zeros((300, 300, 3), dtype = "uint8")

    cv2.circle(frame,(cx,cy),20,(0,0,255),-1)

    cv2.circle(frame,(cx-40,cy-40),10,(0,0,255),-1)
    
    cv2.circle(frame,(cx+40,cy-40),10,(0,0,255),-1)
    
    cv2.circle(frame,(cx+130,cy-40),10,(0,0,255),-1)

    cv2.circle(frame,(cx+150,cy-100),10,(0,0,255),-1)
    
    cv2.circle(frame,(cx+40,cy+40),10,(255,0,0),-1)
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
    
    cv2.imshow("mask",mask)

    #result=cv2.bitwise_and(frame,frame,mask=mask)
    #cv2.imshow("result",result)

    contours,hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contours=sorted(contours, key=lambda x:cv2.contourArea(x), reverse=True)
    cv2.drawContours(frame,contours,-1,(0,255,0),2,-1)
    #print(len(contours))

    
    #cv2.putText(frame,str(count),(50,50),font,1,(0,0,255))
    #put text from str(test) 
    cv2.line(frame,(0,180),(300,180),(0,255,0),2)
    
    for i in range(len(contours)):
        M = cv2.moments(contours[i])
        cxt = int(M['m10'] / M['m00'])
        cyt = int(M['m01'] / M['m00'])
        cv2.circle(frame,(cxt,cyt),3,(255,0,0),-1)
        if(cyt==180):
            #print(cyt)
            count=count+1
            

        """
        (x,y,w,h)=cv2.boundingRect(contours[i])
        x_medium=int((x+x+w)/2)
        y_medium=int((y+y+h)/2)
        cv2.line(frame,(x_medium,0),(x_medium,480),(0,255,0),2)
        cv2.line(frame,(0,y_medium),(300,y_medium),(0,255,0),2)
        """
    #print(count)
    cv2.putText(frame,str(count),(50,50),font,1,(0,0,255))
    cv2.imshow("Frame",frame)
    time.sleep(1/10)
    #cx=cx+1
    cy=cy+1

    if(cy==300):
        cx=100
        cy=100

    #cv2.drawContours(frame),contours,-1,(0,255,0),2)
    #-1 mean all

    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break

cv2.destroyAllWindows()