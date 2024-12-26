import cv2
import matplotlib.pyplot as plt

# Read the noisy image
img2 = cv2.imread('images/noise.png')  # Replace with your image path

# Convert the image to grayscale
gray_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

# Perform histogram equalization
img_eq = cv2.equalizeHist(gray_img2)

# Set up the grid for subplots
grid = plt.GridSpec(3, 4, wspace=0.4, hspace=0.3)

# Original noisy image
plt.subplot(grid[:2, :2])
plt.imshow(gray_img2, cmap='gray')
plt.title('Original Noisy Image')
plt.grid(False)
plt.xticks([])
plt.yticks([])

# Equalized image
plt.subplot(grid[:2, 2:])
plt.imshow(img_eq, cmap='gray')
plt.title('Equalized Image')
plt.grid(False)
plt.xticks([])
plt.yticks([])

# Histogram of the original noisy image
plt.subplot(grid[2, :2])
plt.bar(range(256), cv2.calcHist([gray_img2], [0], None, [256], [0, 256]).ravel())
plt.title('Histogram of Original Image')

# Histogram of the equalized image
plt.subplot(grid[2, 2:])
plt.bar(range(256), cv2.calcHist([img_eq], [0], None, [256], [0, 256]).ravel())
plt.title('Histogram of Equalized Image')

plt.show()