import cv2
import numpy as np
from socket import *

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

host = "192.168.43.105" # set to IP address of target computer
port = 13000
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)

cnt1=0
cnt2=0

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.3,5)

    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        if(conf>50):
            if(Id==1):
                cnt2=0
                cnt1+=1
                Id="Arjun"
                if(cnt1==5):
                    UDPSock.sendto(b'1', addr)
            if(Id==2):
                cnt1=0
                cnt2+=1
                Id="Sashwata"
                if(cnt2==5):
                    UDPSock.sendto(b'2', addr)
            if(Id==3):
                Id="Abdul"
                

        else:
            cnt1=0
            cnt2=0
            Id="Unknown"
        cv2.putText(im,str(Id), (x,y+h),font,1,(0,0,0),5)
    cv2.imshow('im',im)
    if cv2.waitKey(10) & 0xFF==27:
        break
cam.release()
cv2.destroyAllWindows()
