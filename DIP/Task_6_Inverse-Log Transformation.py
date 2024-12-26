import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load an image
image = cv2.imread('images/owl.png', cv2.IMREAD_GRAYSCALE) # Log Transformation
c = 45
log_transformed = c * (np.log(image + 1))

# Convert to 8-bit unsigned integer format
log_transformed = np.uint8(log_transformed)

# Inverse-Log Transformation
inverse_log_transformed = c * (np.exp(log_transformed / c) - 1)

# Convert to 8-bit unsigned integer format
inverse_log_transformed = np.uint8(inverse_log_transformed)

# Display the original and negative images side by side
plt.figure(figsize=(10, 5)) # Create a figure with a specified size
plt.subplot(1, 3, 1) # Subplot for the original image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off') # Turn off axis labels

plt.subplot(1, 3, 2)
plt.imshow(cv2.cvtColor(log_transformed, cv2.COLOR_BGR2RGB))
plt.title("log_transformed")
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(cv2.cvtColor(inverse_log_transformed, cv2.COLOR_BGR2RGB))
plt.title("inverse_log_transformed")
plt.axis('off')

plt.show()