import cv2
import numpy as np 

video = cv2.VideoCapture('/home/nikhom/pythonhome/motion_detection/footage.avi')

first_frame = cv2.createBackgroundSubtractorMOG2(history=20,varThreshold=35 ,detectShadows= True)

while video.isOpened():  

    _,frame = video.read()

    mask = first_frame.apply(frame)

    cv2.imshow("Frame",frame)
    cv2.imshow("mask",mask)

    key = cv2.waitKey(20)
    if  key == 27:
        break

video.release()
cv2.destroyAllWindows()
