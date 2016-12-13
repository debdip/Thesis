import cv2
image = cv2.imread("number.png")
_,image = cv2.threshold(image,70,255,cv2.THRESH_BINARY_INV)
image = cv2.resize(image,(400,400),interpolation=cv2.INTER_AREA)
hog = cv2.HOGDescriptor()
h = hog.compute(image)
print h

