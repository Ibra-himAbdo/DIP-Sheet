import cv2
import matplotlib.pyplot as plt
import numpy as np

# Read the image
img = cv2.imread('images/moon.png')  # Replace with your image path
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply a blur to reduce noise
blur1 = cv2.blur(img, (3, 3))

# Apply the Laplacian operator
laplacian = cv2.Laplacian(blur1, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))  # Convert to uint8

# Create the sharpened image by adding the Laplacian result to the blurred image
img_new = cv2.add(blur1, laplacian)

# Set up the figure for subplots
fig = plt.figure(figsize=(15, 5))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Original Image')
plt.axis('off')

# Laplacian image
plt.subplot(1, 3, 2)
plt.imshow(laplacian, cmap='gray')
plt.title('Laplacian Image')
plt.axis('off')

# Sharpened image
plt.subplot(1, 3, 3)
plt.imshow(img_new)
plt.title('Sharpened Image')
plt.axis('off')

plt.tight_layout()
plt.show()