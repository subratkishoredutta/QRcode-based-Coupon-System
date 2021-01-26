# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:21:19 2021

@author: Asus
"""

##college coupon system MAKERSIDE
import qrcode
import numpy as np
import matplotlib.pyplot as plt
import cv2

qr=qrcode.QRCode(version=1,box_size=10,border=2)
state=0
font = cv2.FONT_HERSHEY_COMPLEX_SMALL

CMP="m&m"

while(True):
    print("\npress\n1-->new coupon\n2-->exit")
    I=int(input(':'))
    if I == 1:
        state+=1
        name=input('name: ')##name of the customer
        food=input('order: ')##each food item contains a code
        ID="ORG_"+str(state)
        string=CMP+"."+name+"."+food+"."+ID
        print(string)
        qr.add_data(string)
        qr.make()
        img=qr.make_image(fill="orange",back_color="white")
        img.save("QR_"+str(ID)+".png")
        img=np.array(img,dtype=np.uint8)*255
        img=cv2.resize(img,(512,512))
        cv2.imshow("QR",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    if I==2:
        print('have a nice day!!')
        break