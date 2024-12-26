import cv2
import matplotlib.pyplot as plt

# Read the image with salt and pepper noise
img = cv2.imread('images/s_p_noise.png')  # Replace with your image path
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Apply mean blur
blur = cv2.blur(img, (5, 5))

# Apply median filter
median = cv2.medianBlur(img, 5)

# Set up the figure for subplots
fig = plt.figure(figsize=(15, 5))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(img)
plt.title('Original Image with Salt and Pepper Noise')
plt.axis('off')

# Image after applying mean blur
plt.subplot(1, 3, 2)
plt.imshow(blur)
plt.title('Mean Blurred Image')
plt.axis('off')

# Image after applying median filter
plt.subplot(1, 3, 3)
plt.imshow(median)
plt.title('Median Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()