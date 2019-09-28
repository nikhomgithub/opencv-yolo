  import cv2
import numpy as np 

video = cv2.VideoCapture('/home/nikhom/pythonhome/motion_detection/footage.avi')

_, frame1 = video.read()
_, frame2 = video.read()

while video.isOpened():  
    diff = cv2.absdiff(frame1,frame2)
    gray = cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    _, thresh = cv2.threshold(blur, 10, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh,None,)
    contours,_ = cv2.findContours(dilated,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.drawContours(frame1,contours,-1,(0,255,0),2)
    #frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #difference = cv2.absdiff(first_frame_gray,frame_gray)

    #cv2.imshow("First frame",first_frame)
    #cv2.imshow("Frame",frame)
    #cv2.imshow("difference",difference)
    cv2.imshow("frame1",frame1)
    cv2.imshow("diff", diff)
    cv2.imshow("dilated",dilated)
    
    frame1 = frame2

    _, frame2 = video.read()


    key = cv2.waitKey(40)
    if  key == 27:
        break

video.release()
cv2.destroyAllWindows()
