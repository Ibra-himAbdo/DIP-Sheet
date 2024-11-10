import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('img1_dev.png', 0)
img2 = cv2.imread('img2_dev.png', 0)

if img1.shape != img2.shape:
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))
plt.figure(figsize=(10, 10))
plt.subplot(131), plt.imshow(img1, cmap='gray')
plt.subplot(132), plt.imshow(img2, cmap='gray')
plt.subplot(133), plt.imshow(img1 / img2, cmap='gray')
plt.show()