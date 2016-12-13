import cv2

image = cv2.imread("number.png")
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) 
_,thresh = cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV) 
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
dilated = cv2.dilate(thresh,kernel,iterations = 13) 
_,contours, hierarchy = cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE) 


i=5
for contour in contours:

    [x,y,w,h] = cv2.boundingRect(contour)
	

    if h>150 and w>150:
        continue


    if h<40 or w<40:
        continue


    cv2.imwrite(str(i)+".jpg",image[y:y+h,x:x+h])
    i=i+1


