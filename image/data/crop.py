import cv2

import numpy as np
ori_filename = 'jor.jpg'

new_filename = 'dn1.jpg'


print("Reading and displaying file: ", ori_filename)

ori_img = cv2.imread(ori_filename)

cv2.imshow(ori_filename,ori_img)


print("Modifying file")

new_img = ori_img

replacement = new_img[30:450, 400:580] # copying a rectengular region

ball = new_img[183:223, 525:565]
cv2.imshow('cropped',replacement)
cv2.imwrite(new_filename,replacement) #save the cropped image

cv2.waitKey(0)

cv2.destroyAllWindows()

