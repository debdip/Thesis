import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread("9.jpg",0)
for it in range(14,22):
	name= str(it)+".jpg"
	image1 = cv2.imread(name,0)
	_,image = cv2.threshold(image,70,255,cv2.THRESH_BINARY_INV)
	_,image1 = cv2.threshold(image1,70,255,cv2.THRESH_BINARY_INV)  
	image = cv2.resize(image,(20,20),interpolation=cv2.INTER_AREA)
	image1 = cv2.resize(image1,(20,20),interpolation=cv2.INTER_AREA)

	image = cv2.dilate(image,(3,3))

	image1 = cv2.dilate(image1,(3,3))
	hist1 = cv2.calcHist([image],[0],None,[256],[0,256])
	hist2 = cv2.calcHist([image1],[0],None,[256],[0,256])
	compare = cv2.compareHist(hist1,hist2,3)
	print compare
