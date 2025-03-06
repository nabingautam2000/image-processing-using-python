import cv2

image = cv2.imread("laptop.jpeg")
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
cv2.imwrite("hsv_output.jpeg", hsv_image)
