import cv2
import matplotlib.pyplot as plt

# Load the original image
original_image = cv2.imread("images/owl.png") # Replace with your image file

# Perform the negative transformation
negative_image = 256 - 1 - original_image

# Display the original and negative images side by side
plt.figure(figsize=(10, 5)) # Create a figure with a specified size
plt.subplot(1, 2, 1) # Subplot for the original image
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.axis('off') # Turn off axis labels

plt.subplot(1, 2, 2) # Subplot for the negative image
plt.imshow(cv2.cvtColor(negative_image, cv2.COLOR_BGR2RGB))
plt.title("Negative Image")
plt.axis('off')

plt.show() # Show the figure with both images