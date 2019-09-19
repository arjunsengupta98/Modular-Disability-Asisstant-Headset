import numpy as np
import cv2
import time
import os
from socket import *

data=0
host = "192.168.43.105"
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
while 1:
    print("Waiting to receive messages...")
    (data, addr) = UDPSock.recvfrom(buf)
#print( "Received message: " + data)

    if(data==b'1'):
        for a in range(1,11):
            img=cv2.imread('DbNew/A_'+str(a)+'.jpg')
            img=cv2.resize(img,(1350,710))
            cv2.imshow('pic '+str(a),img)
            cv2.namedWindow('pic '+str(a))
            cv2.moveWindow('pic '+str(a),0,0)
            k = cv2.waitKey(2000) & 0xff
            cv2.destroyAllWindows()
            if(k==ord('q')):
                break
    if(data==b'2'):

        for a in range(1,11):
            img=cv2.imread('DbNew/B_'+str(a)+'.jpg')
            img=cv2.resize(img,(1350,710))
            cv2.imshow('pic '+str(a),img)
            cv2.namedWindow('pic '+str(a))
            cv2.moveWindow('pic '+str(a),0,0)
            k = cv2.waitKey(2000) & 0xff
            cv2.destroyAllWindows()
            if(k==ord('q')):
                break
    if(k==ord('q')):
        break
