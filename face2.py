import cv2,os
import numpy as np
from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
    faces=[]
    Ids=[]
    for imagePath in imagePaths:
        pilImage=Image.open(imagePath).convert('L')
        imageNp=np.array(pilImage,'uint8')
        Id=int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(imageNp)
        Ids.append(Id)
        cv2.imshow('training',imageNp)
        cv2.waitKey(10)
    return faces,Ids

faces,Ids = getImagesAndLabels('FaceDataBase')
recognizer.train(faces, np.array(Ids))
recognizer.save('trainner/trainner.yml')
