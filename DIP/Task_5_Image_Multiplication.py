import cv2
import numpy as np
import matplotlib.pyplot as plt

xray = cv2.imread('images/dental_xray.jpg', 0)
mask_xray = np.zeros(xray.shape, dtype="uint8")
mask_xray = cv2.rectangle(mask_xray, (400, 200), (650, 700), 1, -1)

plt.figure(figsize=(10, 10))
plt.subplot(131), plt.imshow(xray, cmap='gray'), plt.title('Original Image')
plt.axis('off')
plt.subplot(132), plt.imshow(mask_xray, cmap='gray'), plt.title('Mask')
plt.axis('off')
plt.subplot(133), plt.imshow(cv2.multiply(xray, mask_xray), cmap='gray'), plt.title('Masked Image')
plt.axis('off')
plt.show()