import cv2

image = cv2.imread("dino.jpeg")
blurred = cv2.GaussianBlur(image, (5, 5), 0)  # Kernel size (5x5)
cv2.imwrite("blurred.jpeg", blurred)
