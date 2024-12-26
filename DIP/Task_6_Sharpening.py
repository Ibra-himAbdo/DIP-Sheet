import cv2
import matplotlib.pyplot as plt

# Read the original image
img = cv2.imread('images/lena_gray_256.tif')  # Replace with your image path

# Convert from BGR to RGB
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Convert to grayscale
gray = cv2.cvtColor(RGB_img, cv2.COLOR_BGR2GRAY)

# Remove noise using Gaussian Blur
img_blurred = cv2.GaussianBlur(gray, (3, 3), 0)

# Apply Sobel filter in the x direction
sobelx = cv2.Sobel(img_blurred, cv2.CV_64F, 1, 0, ksize=5)  # x direction
# Apply Sobel filter in the y direction
sobely = cv2.Sobel(img_blurred, cv2.CV_64F, 0, 1, ksize=5)  # y direction

# Set up the figure for subplots
fig = plt.figure(figsize=(15, 5))

# Original image
plt.subplot(1, 3, 1)
plt.imshow(RGB_img)
plt.title('Original Image')
plt.axis('off')

# Sobel X image
plt.subplot(1, 3, 2)
plt.imshow(sobelx, cmap='gray')
plt.title('Sobel X Filtered Image')
plt.axis('off')

# Sobel Y image
plt.subplot(1, 3, 3)
plt.imshow(sobely, cmap='gray')
plt.title('Sobel Y Filtered Image')
plt.axis('off')

plt.tight_layout()
plt.show()