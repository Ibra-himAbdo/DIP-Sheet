import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('images/dip_xe.png')  # Replace with your image path
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Step 1: Blur the original image
blur = cv2.GaussianBlur(img, (25, 25), 0)

# Step 2: Subtract the blurred image from the original
mask = cv2.subtract(img, blur)

# Step 3: Add the mask to the original image
sharpened_image = cv2.add(img, mask)

# Highboost filtering with k > 1
highboost_image = cv2.add(img, 5 * mask)

# Set up the figure for subplots
fig = plt.figure(figsize=(15, 10))

# Original image
plt.subplot(1, 5, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

# Blurred image
plt.subplot(1, 5, 2)
plt.imshow(blur)
plt.title('Blurred Image')
plt.axis('off')

# Mask image
plt.subplot(1, 5, 3)
plt.imshow(mask)
plt.title('Mask Image')
plt.axis('off')

# Sharpened image
plt.subplot(1, 5, 4)
plt.imshow(sharpened_image)
plt.title('Sharpened Image')
plt.axis('off')

# Highboost filtered image
plt.subplot(1, 5, 5)
plt.imshow(highboost_image)
plt.title('Highboost Filtered Image (k=5)')
plt.axis('off')

plt.tight_layout()
plt.show()