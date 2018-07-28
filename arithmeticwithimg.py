import cv2
import numpy as np

img1 = cv2.imread(r'C:\Users\Rag9704\Desktop\python.png')
img2 = cv2.imread(r'C:\Users\Rag9704\Desktop\HackBGRT-Windows-10-UEFI-boot-logo-changer.png')


rows,cols,channels = img1.shape
roi = img2[0:rows,0:cols]

img2gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
ret , mask = cv2.threshold(img2gray,220,255,cv2.THRESH_BINARY_INV)

mask_inv=cv2.bitwise_not(mask)
img2_bg= cv2.bitwise_and(roi , roi ,mask=mask_inv)
img1_fg = cv2.bitwise_and(img1 , img1 , mask=mask)

dst = cv2.add(img2_bg,img1_fg)
img2[0:rows,0:cols]=dst

cv2.imshow('res',img2)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('img2_bg',img2_bg)
cv2.imshow('img1_fg',img1_fg)
cv2.imshow('dst',dst)


#cv2.imshow('mask',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
