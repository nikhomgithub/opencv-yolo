import cv2
import numpy as np 
import time

def nothing(x):
    pass

lab_k = [1,3,5,7,9,11,13,15,17,19,21]
key=0

blur_list=[1,3,5,7,9,11,13,15,17,19,21]

video=cv2.VideoCapture('footage.avi')

cv2.namedWindow("Trackbar")

cv2.createTrackbar("Canny-L","Trackbar",55,255,nothing)
cv2.createTrackbar("Canny-H","Trackbar",100,255,nothing)
cv2.createTrackbar("Lap-K","Trackbar",6,10,nothing)

cv2.createTrackbar("=====","Trackbar",0,1,nothing)

cv2.createTrackbar("Blur-size","Trackbar",2,10,nothing)
cv2.createTrackbar("Blur-sigma","Trackbar",0,100,nothing)
cv2.createTrackbar("thres-hold","Trackbar",20,255,nothing)
cv2.createTrackbar("dilat-iter","Trackbar",1,10,nothing)

ret,frame1 = video.read()
frame1_gray = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
frame1_canny = cv2.Canny(frame1_gray,55,100)

ret,frame2 = video.read()
frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
frame2_canny = cv2.Canny(frame2_gray,55,100)

while video.isOpened():
    ret,frame = video.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    c_l = cv2.getTrackbarPos("Canny-L","Trackbar") 
    c_h = cv2.getTrackbarPos("Canny-H","Trackbar")
    l_k = cv2.getTrackbarPos("Lap-K","Trackbar")

    laplacian = cv2.Laplacian(frame_gray,cv2.CV_64F,ksize=lab_k[l_k])
    canny = cv2.Canny(frame_gray,c_l,c_h)

    b_sigma = cv2.getTrackbarPos("Blur-sigma","Trackbar")
    b_size = cv2.getTrackbarPos("Blur-size","Trackbar")
    thresh_value = cv2.getTrackbarPos("thres-hold","Trackbar")
    iter = cv2.getTrackbarPos("dilat-iter","Trackbar")

   #==================================
    diff = cv2.absdiff(frame1,frame2)
    diff_gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    diff_blur = cv2.GaussianBlur(diff_gray,(blur_list[b_size],blur_list[b_size]),b_sigma )
    _,thresh = cv2.threshold(diff_blur,thresh_value,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh, None, iterations=iter)
    contours,_ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(frame1,contours,-1,(0,255,0),2)

    for contour in contours:
        if cv2.contourArea(contour) <1000:
            continue
        else :
            (x,y,w,h) = cv2.boundingRect(contour)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cxt = int((x+x+h)/2)
            cyt = int((y+y+h)/2)
            cv2.circle(frame,(cxt,cyt),3,(255,0,0),-1)


    cv2.imshow('frame',frame)
    cv2.imshow('frame laplacian',laplacian)
    cv2.imshow('Canny',canny)
    

    cv2.imshow('diff',dilated)
    cv2.imshow('frame 1',frame1)
    
    diff_canny = cv2.absdiff(frame1_canny,frame2_canny)
  
    frame1 = frame2
    frame1_canny = frame2_canny
    

    ret,frame2 = video.read()
    frame2_gray = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)    
    frame2_canny = cv2.Canny(frame2_gray,c_l,c_h)
   
    cv2.imshow('diff_canny',diff_canny)


    key = cv2.waitKey(40)
    if  key == 27:
        break



cv2.destroyAllWindows()
video.release()
