# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 21:56:30 2021

@author: Asus
"""

from tkinter import *
import qrcode
import numpy as np
import cv2
from PIL import Image,ImageTk
qr=qrcode.QRCode(version=1,box_size=10,border=2)

root=Tk()
root.title('AEC canteen')
root.geometry("220x200")

CMP="m&m"

state=IntVar()
state.set(0)
def getQRcode():
        val=state.get()
        state.set(val+1)
        req=state.get()
        name=nameval.get()##name of the customer
        food=foodval.get()##each food item contains 
        ID=CMP+str(req)
        string=CMP+"."+name+"."+food+"."+ID
        qr.add_data(string)
        qr.make()
        img=qr.make_image(fill="orange",back_color="white")
        img.save("QR_"+str(ID)+".png")
        img=np.array(img,dtype=np.uint8)*255
        img=cv2.resize(img,(512,512)) 
        cv2.imshow("QR",img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

Label(root,text="Coupon",font="comicsansms 13 bold",pady=15).grid(row=0,column=3)
name=Label(root,text="Name",padx=15,pady=10).grid(row=1,column=2)
food=Label(root,text="Food",padx=15,pady=10).grid(row=2,column=2)


nameval=StringVar()
foodval=StringVar()

namentry=Entry(root,textvariable=nameval).grid(row=1,column=3)
foodentry=Entry(root,textvariable=foodval).grid(row=2,column=3)

Button(text=" QRcode ",command=getQRcode).grid(row=3,column=3)

root.mainloop()