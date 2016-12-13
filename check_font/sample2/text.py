import cv2

image = cv2.imread("number.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
_,thresh = cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV) 
thresh1 = cv2.adaptiveThreshold(gray,255,1,1,11,2)
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 1) 
_,contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) 


cv2.imshow("image",thresh)
cv2.imshow("img",thresh1)
cv2.imshow("dilate",dilated)
cv2.waitKey(0)

