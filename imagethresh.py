import cv2

image = cv2.imread("pig.jpeg", 0)
_, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
cv2.imwrite("threshold.jpeg", thresh)