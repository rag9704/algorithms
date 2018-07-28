import cv2
import numpy as np

cap=cv2.VideoCapture(0)

while True :
    _, frame = cap.read()
    hsv =cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)  #hue saturation value

    lower_red=np.array([0,50,50])
    upper_red=np.array([10,255,180])

    """dark_red=np.uintB([[[12,22,121]]])
    dark_red=cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)"""

    mask = cv2.inRange(hsv,lower_red,upper_red)
    res=cv2.bitwise_and(frame,frame,mask=mask)

    kernel=np.ones((5,5),np.uint8)
    erosin = cv2.erode(mask,kernel,iterations=1)
    dilation = cv2.dilate(mask,kernel,iterations=1)

    opening = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) #for bg positive
    closong = cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)

    """cv2.imshow('Tophat',tophat)
    cv2.imshow('Blackhat',blackhat)"""
    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('ero',erosin)
    cv2.imshow('dil',dilation)
    cv2.imshow('open',opening)
    cv2.imshow('close',closong)
    k = cv2.waitKey(0)
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
