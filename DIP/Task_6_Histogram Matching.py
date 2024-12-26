import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import exposure

# Function to load and convert an image to grayscale
def load_image(number):
    img = cv2.imread(f"images/imgs/{number}.bmp")  # Adjust the path as needed
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return gray

# Load the source and destination images
src = load_image(2)  # Source image
dst = load_image(1)  # Reference image for histogram matching

# Perform histogram matching
matched_src = exposure.match_histograms(src, dst)

# Set up the grid for subplots
fig, axs = plt.subplots(3, 2, figsize=(10, 12))

# Original source image
axs[0, 0].imshow(src, cmap='gray')
axs[0, 0].set_title('Source Image')
axs[0, 0].axis('off')

# Reference destination image
axs[0, 1].imshow(dst, cmap='gray')
axs[0, 1].set_title('Reference Image')
axs[0, 1].axis('off')

# Matched image
axs[1, 0].imshow(matched_src, cmap='gray')
axs[1, 0].set_title('Matched Image')
axs[1, 0].axis('off')

# Histogram of the source image
axs[2, 0].hist(src.ravel(), bins=256, color='black', alpha=0.7)
axs[2, 0].set_title('Histogram of Source Image')

# Histogram of the matched image
axs[2, 1].hist(matched_src.ravel(), bins=256, color='black', alpha=0.7)
axs[2, 1].set_title('Histogram of Matched Image')

plt.tight_layout()
plt.show()