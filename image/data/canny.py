import cv2

import numpy as np
img = cv2.imread('number.jpg')
img1='num1.jpg'
#cv2.imshow("orig", img)

img = cv2.blur(img,(2,2))
gray_seg = cv2.Canny(img, 450, 450)
cv2.imshow("orig", gray_seg)
cv2.imwrite(img1,gray_seg)
cv2.waitKey(0)
