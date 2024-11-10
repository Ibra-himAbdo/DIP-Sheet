import cv2
import matplotlib.pyplot as plt

img1_sub = cv2.imread('img1_sub.png', 0)
img2_sub = cv2.imread('img2_sub.png', 0)

# I made this because I took screenshots from the sheet
# Print the shapes of the images
print(f"Image 1 shape: {img1_sub.shape}")
print(f"Image 2 shape: {img2_sub.shape}")

# Resize img2_sub to match img1_sub if they are different sizes
if img1_sub.shape != img2_sub.shape:
    img2_sub = cv2.resize(img2_sub, (img1_sub.shape[1], img1_sub.shape[0]))

changes = cv2.subtract(img1_sub, img2_sub)

plt.figure(figsize=(20, 20))
plt.subplot(1, 3, 1), plt.imshow(img1_sub, cmap='gray')
plt.subplot(1, 3, 2), plt.imshow(img2_sub, cmap='gray')
plt.subplot(1, 3, 3), plt.imshow(changes, cmap='gray')
plt.show()