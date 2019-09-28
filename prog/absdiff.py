import cv2
import numpy as np 

video = cv2.VideoCapture('/home/nikhom/pythonhome/motion_detection/footage.avi')

_, first_frame = video.read()
first_frame_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)

while video.isOpened():  

    _,frame = video.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    difference = cv2.absdiff(first_frame_gray,frame_gray)

    cv2.imshow("First frame",first_frame)
    cv2.imshow("Frame",frame)
    cv2.imshow("difference",difference)


    key = cv2.waitKey(30)
    if  key == 27:
        break

video.release()
cv2.destroyAllWindows()
