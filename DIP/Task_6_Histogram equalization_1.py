import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('images/equl.png')

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Perform histogram equalization
img_eq = cv2.equalizeHist(gray_img)


# Set up the grid for subplots
grid = plt.GridSpec(3, 4, wspace=0.4, hspace=0.3)

# Original image
plt.subplot(grid[:2, :2])
plt.imshow(gray_img, cmap='gray')
plt.grid(False)
plt.xticks([])
plt.yticks([])
plt.title('Original Image')

# Equalized image
plt.subplot(grid[:2, 2:])
plt.imshow(img_eq, cmap='gray')
plt.grid(False)
plt.xticks([])
plt.yticks([])
plt.title('Equalized Image')

# Histogram of the original image
plt.subplot(grid[2, :2])
plt.bar(range(256), cv2.calcHist([gray_img], [0], None, [256], [0, 256]).ravel())
plt.title('Histogram of Original Image')

# Histogram of the equalized image
plt.subplot(grid[2, 2:])
plt.bar(range(256), cv2.calcHist([img_eq], [0], None, [256], [0, 256]).ravel())
plt.title('Histogram of Equalized Image')

plt.show()