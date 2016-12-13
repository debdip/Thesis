import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread("6.jpg",0)
image1 = cv2.imread("8.jpg",0)
_,image = cv2.threshold(image,70,255,cv2.THRESH_BINARY_INV)
_,image1 = cv2.threshold(image1,70,255,cv2.THRESH_BINARY_INV)  
image = cv2.resize(image,(20,20),interpolation=cv2.INTER_AREA)
image1 = cv2.resize(image1,(20,20),interpolation=cv2.INTER_AREA)
res = cv2.matchTemplate(image,image1,cv2.TM_CCOEFF)
print res
image = cv2.dilate(image,(3,3))

image1 = cv2.dilate(image1,(3,3))
cv2.imshow('image',image)
cv2.imshow('image1',image1)
cv2.waitKey(0)
hist1 = cv2.calcHist([image],[0],None,[256],[0,256])
hist2 = cv2.calcHist([image1],[0],None,[256],[0,256])
compare = cv2.compareHist(hist1,hist2,1)
print compare
