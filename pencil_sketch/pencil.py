import cv2
def dodgeV2(image, mask):
	return cv2.divide(image, 255-mask, scale=256)
img_rgb = cv2.imread("lol.jpg")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
img_gray_inv = 255 - img_gray
img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(57, 57),sigmaX=0, sigmaY=0)
img_blend = dodgeV2(img_gray, img_blur)
cv2.imwrite("lol1.jpg",img_blend)
cv2.waitKey(0)
