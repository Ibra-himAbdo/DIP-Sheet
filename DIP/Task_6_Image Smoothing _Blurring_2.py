import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
img = cv2.imread('images/early_1800.jpg')  # Replace with your image path
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Create a 5x5 mean filter kernel
kernel = np.ones((5, 5), np.float32) / 25  # 5x5 kernel with equal weights

# Apply the mean filter using filter2D
dst = cv2.filter2D(img, -1, kernel)

# Apply the mean blur using cv2.blur
blur = cv2.blur(img, (5, 5))

# Set up the figure for subplots
fig = plt.figure(figsize=(20, 20))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

# Image after applying the mean filter
plt.subplot(1, 3, 2)
plt.imshow(dst)
plt.title('Mean Filtered Image (5x5 Kernel)')
plt.axis('off')

# Image after applying the blur
plt.subplot(1, 3, 3)
plt.imshow(blur)
plt.title('Blurred Image (5x5 Kernel)')
plt.axis('off')

plt.tight_layout()
plt.show()