import cv2
import matplotlib.pyplot as plt

lena = cv2.imread('images/lena_gray_256.tif', 0)
plt.figure(figsize=(20, 20))
plt.subplot(1, 3, 1), plt.imshow(lena, cmap='gray')
plt.subplot(1, 3, 2), plt.imshow(cv2.subtract(lena, 128), cmap='gray')
plt.subplot(1, 3, 3), plt.imshow(lena - 128, cmap='gray')
plt.show()