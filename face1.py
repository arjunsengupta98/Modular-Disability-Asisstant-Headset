import numpy as np
import cv2

f1 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
c = cv2.VideoCapture(0)
img=cv2.imread('download.jpeg')
gray=cv2.imread('download.jpeg')
id=input('Enter user id')
sampleNum=0
while 1:
    ret, img = c.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = f1.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        sampleNum=sampleNum+1
        cv2.imwrite('FaceDataBase/User.'+str(id)+'.'+str(sampleNum)+'.jpg',gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.waitKey(100)
    cv2.imshow('img',img)
    cv2.waitKey(1)
    if(sampleNum>60):
        break

c.release()
cv2.destroyAllWindows()
