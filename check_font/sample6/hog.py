import cv2
image = cv2.imread("14.jpg")

image = cv2.resize(image,(400,400),interpolation=cv2.INTER_AREA)
hog = cv2.HOGDescriptor()
h = hog.compute(image)
print h

