import cv2
import numpy as np
import matplotlib.pyplot as plt

rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)

circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)

plt.figure(figsize=(20, 20))

plt.subplot(2,3,1).set_title("Rectangle"),plt.imshow(rectangle,cmap='gray')
plt.subplot(2,3,2).set_title("Circle"), plt.imshow(circle,cmap='gray')
plt.subplot(2,3,3).set_title("And"), plt.imshow(cv2.bitwise_and(rectangle, circle),cmap='gray')
plt.subplot(2,3,4).set_title("OR"), plt.imshow(cv2.bitwise_or(rectangle, circle),cmap='gray')
plt.subplot(2,3,5).set_title("XOR"), plt.imshow(cv2.bitwise_xor(rectangle, circle),cmap='gray')
plt.subplot(2,3,6).set_title("NOT"), plt.imshow(cv2.bitwise_not(circle),cmap='gray')

plt.show()
