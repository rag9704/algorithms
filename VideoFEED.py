import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')


while True:
    ret,frame=cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #OPTIONAL
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)#optinal

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
