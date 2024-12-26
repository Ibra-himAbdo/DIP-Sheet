import cv2
import numpy as np
import matplotlib.pyplot as plt

# Read an image
image = cv2.imread('images/sample_image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply gamma correction (e.g., gamma = 1.5)
gamma = 2
adjusted_image = np.power(image / 255.0, gamma) * 255.0
adjusted_image = adjusted_image.astype(np.uint8)

gamma2 = 4
adjusted_image2 = np.power(image / 255.0, gamma2) * 255.0
adjusted_image2 = adjusted_image2.astype(np.uint8)

plt.figure(figsize=(10, 5)) # Create a figure with a specified size
plt.subplot(1, 3, 1) # Subplot for the original image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

plt.subplot(1, 3, 2) # Subplot for the adjusted image
plt.imshow(cv2.cvtColor(adjusted_image, cv2.COLOR_BGR2RGB))
plt.title("adjusted_image gamma = 2")

plt.subplot(1, 3, 3) # Subplot for the adjusted image with gamma = 4
plt.imshow(cv2.cvtColor(adjusted_image2, cv2.COLOR_BGR2RGB))
plt.title("adjusted_image gamma = 4")
plt.axis('off')

plt.show()