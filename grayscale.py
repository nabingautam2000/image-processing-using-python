import cv2

# Load image
image = cv2.imread("dino.jpeg")

# Save image
cv2.imwrite("dino.jpeg", image)
