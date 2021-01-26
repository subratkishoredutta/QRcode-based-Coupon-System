# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 19:49:06 2021

@author: Asus
"""

import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar
import matplotlib.pyplot as plt
IMG_H=IMG_W=600
channels=3
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
#img=cv2.imread('QR.png')




cam=cv2.VideoCapture(0)

while(True):
    _,frame=cam.read()
    DO=pyzbar.decode(frame)
    im=None
    for obj in DO:
        im=obj.data
    if im!=None:
        print('detected')
        im=str(im)
        CMP,name,food,ID=im[2:-1].split('.')
        
        img=np.ones((IMG_H,IMG_W,channels),dtype=np.uint8)
        img=img*50
        img = cv2.putText(img,CMP,(IMG_W-150*len(CMP),520),font,10,(0,165,241),2,cv2.LINE_AA)
        img = cv2.putText(img,name,(50,256),font,4,(0,255,255),5,cv2.LINE_AA)
        img = cv2.putText(img,ID,(128,256+128),font,2,(0,255,255),3,cv2.LINE_AA)
        img = cv2.putText(img,food,(400,100),font,6,(0,255,255),3,cv2.LINE_AA)
        cv2.resize(img,(512,512))
        cv2.imshow('info',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    print('ND')
    
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()    

