import sys

import numpy as np
import cv2

image = cv2.imread("0.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
_,thresh = cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV) 
_,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
image1 = cv2.imread("1.png")
gray1 = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY) 
_,thresh1 = cv2.threshold(gray1,70,255,cv2.THRESH_BINARY_INV) 
_,contours1, hierarchy1 = cv2.findContours(thresh1,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 

samples =  np.empty((0,100))
responses = []
keys = [i for i in range(48,58)]

for cnt in contours:
    
        [x,y,w,h] = cv2.boundingRect(cnt)
       	cv2.rectangle(image,(x,y),(x+w+2,y+h+2),(0,0,255),2)
       	roi = thresh[y:y+h+2,x:x+w+2]
    
        roismall = cv2.resize(roi,(10,10))
        cv2.imshow('norm',image)
        key = cv2.waitKey(0)

        if key == 27:  # (escape to quit)
            sys.exit()
        elif key in keys:
            responses.append(int(chr(key)))
            sample = roismall.reshape((1,100))
            samples = np.append(samples,sample,0)
for cnt in contours1:
    
        [x,y,w,h] = cv2.boundingRect(cnt)
       	cv2.rectangle(image1,(x,y),(x+w+2,y+h+2),(0,0,255),2)
       	roi = thresh1[y:y+h+2,x:x+w+2]
    
        roismall = cv2.resize(roi,(10,10))
        cv2.imshow('norm',image1)
        key = cv2.waitKey(0)

        if key == 27:  # (escape to quit)
            sys.exit()
        elif key in keys:
            responses.append(int(chr(key)))
            sample = roismall.reshape((1,100))
            samples = np.append(samples,sample,0)

image2 = cv2.imread("2.png")
gray2 = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY) 
_,thresh2 = cv2.threshold(gray2,70,255,cv2.THRESH_BINARY_INV) 
_,contours2, hierarchy2 = cv2.findContours(thresh2,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
for cnt in contours2:
    
        [x,y,w,h] = cv2.boundingRect(cnt)
       	cv2.rectangle(image2,(x,y),(x+w+2,y+h+2),(0,0,255),2)
       	roi = thresh1[y:y+h+2,x:x+w+2]
    
        roismall = cv2.resize(roi,(10,10))
        cv2.imshow('norm',image2)
        key = cv2.waitKey(0)

        if key == 27:  # (escape to quit)
            sys.exit()
        elif key in keys:
            responses.append(int(chr(key)))
            sample = roismall.reshape((1,100))
            samples = np.append(samples,sample,0)
image3 = cv2.imread("3.png")
gray3 = cv2.cvtColor(image3,cv2.COLOR_BGR2GRAY) 
_,thresh3 = cv2.threshold(gray3,70,255,cv2.THRESH_BINARY_INV) 
_,contours3, hierarchy3 = cv2.findContours(thresh3,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
for cnt in contours3:
    
        [x,y,w,h] = cv2.boundingRect(cnt)
       	cv2.rectangle(image3,(x,y),(x+w+2,y+h+2),(0,0,255),2)
       	roi = thresh1[y:y+h+2,x:x+w+2]
    
        roismall = cv2.resize(roi,(10,10))
        cv2.imshow('norm',image3)
        key = cv2.waitKey(0)

        if key == 27:  # (escape to quit)
            sys.exit()
        elif key in keys:
            responses.append(int(chr(key)))
            sample = roismall.reshape((1,100))
            samples = np.append(samples,sample,0)
image4 = cv2.imread("4.png")
gray4 = cv2.cvtColor(image4,cv2.COLOR_BGR2GRAY) 
_,thresh4 = cv2.threshold(gray4,70,255,cv2.THRESH_BINARY_INV) 
_,contours4, hierarchy4 = cv2.findContours(thresh4,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
for cnt in contours4:
    
        [x,y,w,h] = cv2.boundingRect(cnt)
       	cv2.rectangle(image4,(x,y),(x+w+2,y+h+2),(0,0,255),2)
       	roi = thresh4[y:y+h+2,x:x+w+2]
    
        roismall = cv2.resize(roi,(10,10))
        cv2.imshow('norm',image4)
        key = cv2.waitKey(0)

        if key == 27:  # (escape to quit)
            sys.exit()
        elif key in keys:
            responses.append(int(chr(key)))
            sample = roismall.reshape((1,100))
            samples = np.append(samples,sample,0)

image5 = cv2.imread("5.png")
gray5 = cv2.cvtColor(image5,cv2.COLOR_BGR2GRAY) 
_,thresh5 = cv2.threshold(gray5,70,255,cv2.THRESH_BINARY_INV) 
_,contours5, hierarchy5 = cv2.findContours(thresh5,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
for cnt in contours5:
    
        [x,y,w,h] = cv2.boundingRect(cnt)
       	cv2.rectangle(image5,(x,y),(x+w+2,y+h+2),(0,0,255),2)
       	roi = thresh5[y:y+h+2,x:x+w+2]
    
        roismall = cv2.resize(roi,(10,10))
        cv2.imshow('norm',image5)
        key = cv2.waitKey(0)

        if key == 27:  # (escape to quit)
            sys.exit()
        elif key in keys:
            responses.append(int(chr(key)))
            sample = roismall.reshape((1,100))
            samples = np.append(samples,sample,0)

image6 = cv2.imread("6.png")
gray6 = cv2.cvtColor(image6,cv2.COLOR_BGR2GRAY) 
_,thresh6 = cv2.threshold(gray6,70,255,cv2.THRESH_BINARY_INV) 
_,contours6, hierarchy6 = cv2.findContours(thresh6,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
for cnt in contours6:
    
        [x,y,w,h] = cv2.boundingRect(cnt)
       	cv2.rectangle(image6,(x,y),(x+w+2,y+h+2),(0,0,255),2)
       	roi = thresh6[y:y+h+2,x:x+w+2]
    
        roismall = cv2.resize(roi,(10,10))
        cv2.imshow('norm',image6)
        key = cv2.waitKey(0)

        if key == 27:  # (escape to quit)
            sys.exit()
        elif key in keys:
            responses.append(int(chr(key)))
            sample = roismall.reshape((1,100))
            samples = np.append(samples,sample,0)

image7 = cv2.imread("7.png")
gray7 = cv2.cvtColor(image7,cv2.COLOR_BGR2GRAY) 
_,thresh7 = cv2.threshold(gray7,70,255,cv2.THRESH_BINARY_INV) 
_,contours7, hierarchy7 = cv2.findContours(thresh7,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
for cnt in contours7:
    
        [x,y,w,h] = cv2.boundingRect(cnt)
       	cv2.rectangle(image7,(x,y),(x+w+2,y+h+2),(0,0,255),2)
       	roi = thresh7[y:y+h+2,x:x+w+2]
    
        roismall = cv2.resize(roi,(10,10))
        cv2.imshow('norm',image7)
        key = cv2.waitKey(0)

        if key == 27:  # (escape to quit)
            sys.exit()
        elif key in keys:
            responses.append(int(chr(key)))
            sample = roismall.reshape((1,100))
            samples = np.append(samples,sample,0)

image8 = cv2.imread("8.png")
gray8 = cv2.cvtColor(image8,cv2.COLOR_BGR2GRAY) 
_,thresh8 = cv2.threshold(gray8,70,255,cv2.THRESH_BINARY_INV) 
_,contours8, hierarchy8 = cv2.findContours(thresh8,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
for cnt in contours8:
    
        [x,y,w,h] = cv2.boundingRect(cnt)
       	cv2.rectangle(image8,(x,y),(x+w+2,y+h+2),(0,0,255),2)
       	roi = thresh8[y:y+h+2,x:x+w+2]
    
        roismall = cv2.resize(roi,(10,10))
        cv2.imshow('norm',image8)
        key = cv2.waitKey(0)

        if key == 27:  # (escape to quit)
            sys.exit()
        elif key in keys:
            responses.append(int(chr(key)))
            sample = roismall.reshape((1,100))
            samples = np.append(samples,sample,0)

image9 = cv2.imread("9.png")
gray9 = cv2.cvtColor(image9,cv2.COLOR_BGR2GRAY) 
_,thresh9 = cv2.threshold(gray9,70,255,cv2.THRESH_BINARY_INV) 
_,contours9, hierarchy9 = cv2.findContours(thresh9,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 
for cnt in contours9:
    
        [x,y,w,h] = cv2.boundingRect(cnt)
       	cv2.rectangle(image9,(x,y),(x+w+2,y+h+2),(0,0,255),2)
       	roi = thresh9[y:y+h+2,x:x+w+2]
    
        roismall = cv2.resize(roi,(10,10))
        cv2.imshow('norm',image9)
        key = cv2.waitKey(0)

        if key == 27:  # (escape to quit)
            sys.exit()
        elif key in keys:
            responses.append(int(chr(key)))
            sample = roismall.reshape((1,100))
            samples = np.append(samples,sample,0)

responses = np.array(responses,np.float32)
responses = responses.reshape((responses.size,1))

print "training complete"

np.savetxt('generalsamples.data',samples)
np.savetxt('generalresponses.data',responses)



    


