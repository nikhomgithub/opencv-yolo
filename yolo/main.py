#https://pysource.com/2019/06/27/yolo-object-detection-using-opencv-with-python/
#https://www.youtube.com/watch?v=h56M5iUVgGs
#https://gist.github.com/leandrobmarinho/26bd5eb9267654dbb9e37f34788486b5
#git clone https://github.com/pjreddie/darknet
import cv2
import numpy as np
import time
#load yolo algorithm as net
net = cv2.dnn.readNet("yolov3.weights","yolov3.cfg")

#get class from coco.names file by read it only
classes=[]
with open("coco.names","r") as f:
    classes=[line.strip() for line in f.readlines()]
# classes=['person', 'bicycle', 'car', 'motorbike',....]

#create model's layer
layer_names=net.getLayerNames()
output_layers=[layer_names[i[0]-1] for i in net.getUnconnectedOutLayers()]
colors=np.random.uniform(0,255,size=(len(classes),3))

cap=cv2.VideoCapture(0)#for video

while True:
    
    _,img=cap.read()#for video
    
    #load image we want to test
    #img=cv2.imread("office.jpg")#for image
    #img=cv2.resize(img,None,fx=1.1,fy=1.1)#for image
    height,width,channel=img.shape

    #Detecting objects in image (blob)
    blob=cv2.dnn.blobFromImage(img,0.0032,(416,416),(0,0,0),True,crop=False)

    """
    #actually no need for this blob
    for b in blob:
        for n, img_blob in enumerate(b):
            cv2.imshow(str(n),img_blob)
    """

    #put image(blob) in model
    net.setInput(blob)
    #get output from output_layers
    outs=net.forward(output_layers)
    #outs is output from model it is array of object

    class_ids=[]
    confidences=[]
    boxes=[]
    circles=[]

    #output-object array has many information socres,confidence,centerX,centerY,height,weidht
    #we process by run through outs to get value that we need
    #select only value of outs where confidence > 0.5 only 
    #x,y,w,h for retangular
    #center_x,center_y for circle
    #class_id for for-loop and refer to classes
    #confidences for confidence value
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id=np.argmax(scores)
            confidence=scores[class_id]
            #select only result of confidence > 0.5
            if confidence>0.5:
                center_x=int(detection[0]*width)
                center_y=int(detection[1]*height)
                w=int(detection[2]*width)
                h=int(detection[3]*height)

                #try to circle detected-object center
                #cv2.circle(img,(center_x,center_y),10,(0,255,0),2)

                #try to rectangle detected-object center
                x=int(center_x-w/2)
                y=int(center_y-h/2)
                #cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                
                #keep values in array of boxes, confidences, class_ids
                boxes.append([x,y,w,h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                circles.append([center_x,center_y])

    print(len(boxes))
    #print(boxes)
    #print(confidences)

    #try to reduce-double box due to noice in image mask 
    indexes=cv2.dnn.NMSBoxes(boxes,confidences,0.5,0.4)
    print(indexes)
    font=cv2.FONT_HERSHEY_PLAIN
    #let's output what we want on img
    for i in range(len(boxes)):
        if i in indexes:
            x,y,w,h=boxes[i]
            label=str(classes[class_ids[i]])
            color=colors[i]
            cv2.rectangle(img,(x,y),(x+w,y+h),color,1)
            cv2.putText(img,label,(x,y+30),font,1,(0,0,255),1)

    cv2.imshow("img",img)
    #time.sleep(1/10)

#while True:
    key=cv2.waitKey(1)
    if key==27: #27 is ESC
        break

cap.release()#for video

cv2.destroyAllWindows()