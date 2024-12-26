import cv2
import matplotlib.pyplot as plt

# Read the image
img = cv2.imread('images/early_1800.jpg')  # Replace with your image path
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

gblur = cv2.GaussianBlur(img, (5, 5), 0)
plt.imshow(gblur)
plt.axis('off')
plt.show()