import sys

import numpy as np
import cv2

image = cv2.imread("number.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
_,thresh = cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV) 
cv2.imshow("show",thresh)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 13) 
_,contours, hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 


samples =  np.empty((0,100))
responses = []
keys = [i for i in range(48,58)]

for cnt in contours:
    
        [x,y,w,h] = cv2.boundingRect(cnt)
       	cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255),2)
       	roi = thresh[y:y+h,x:x+w]
    
        roismall = cv2.resize(roi,(10,10))
        cv2.imshow('norm',image)
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



    


