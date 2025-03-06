import cv2

image = cv2.imread("horse.jpeg", 0)
adaptive = cv2.adaptiveThreshold(
    image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
)
cv2.imwrite("adaptive_thresh.jpeg", adaptive)
