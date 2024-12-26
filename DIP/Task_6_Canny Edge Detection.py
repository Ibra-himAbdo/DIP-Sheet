import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read image from disk
img = cv2.imread('images/panda.png')  # Replace with your image path
image_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply Canny edge detection
edges = cv2.Canny(image=image_rgb, threshold1=100, threshold2=700)

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# Plot the original image
axs[0].imshow(image_rgb)
axs[0].set_title('Original Image')
axs[0].axis('off')

# Plot the edges
axs[1].imshow(edges, cmap='gray')
axs[1].set_title('Image Edges')
axs[1].axis('off')

# Display the subplots
plt.tight_layout()
plt.show()