import numpy as np
import cv2
import pickle
import pickle as pkl
import time
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")
labels={}
detected_faces = [];
with open("labels.pkl","rb") as f:
    og_labels=pickle.load(f)
    labels={v:k for k,v in og_labels.items()}
cap=cv2.VideoCapture(0)
i=0
while cv2.waitKey(1)<0:
    i =i+1
    ret,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
    for x,y,w,h in faces:
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=frame[y:y+h,x:x+w]
        id_,conf=recognizer.predict(roi_gray)
        if conf>=45:
            detected_faces.append(labels[id_])
            print(labels[id_])
            font=cv2.FONT_HERSHEY_SIMPLEX
            name=labels[id_]
            color=(0,255,0)
            stroke=2
            cv2.putText(frame,name,(x,y),font,1,color,stroke,cv2.LINE_AA)
        # my_item=cv2.imwrite("alton2.jpg",roi_gray)
        # my_item = cv2.imwrite("alton3.jpg", roi_color)
        color=(255,0,0)
        stroke=2
        cv2.rectangle(frame,(x,y),(x+w,y+h),color,stroke)
    cv2.imshow('frame',frame)
    if i==100:
    # if cv2.waitKey(0):
        break
cap.release()
cv2.destroyAllWindows()
print(detected_faces)