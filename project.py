from array import array
import code
import cv2
import numpy as np
from pyzbar.pyzbar import decode

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,48)

while True:
    success,img = cap.read()
    
    code = decode(img)
    for qrCode in code:
        myText = qrCode.data.decode('utf-8')
        pts = np.array([qrCode.polygon],np.int32)
        rp = qrCode.rect
        cv2.polylines(img,[pts],True,(0,255,0),2)
        cv2.putText(img,myText,(rp[0],rp[1],cv2.FONT_HERSHEY_PLAIN),0.9,(0,255,0),1)
        print(myText)

    cv2.imshow('Result Image',img)
    cv2.waitKey(2)






