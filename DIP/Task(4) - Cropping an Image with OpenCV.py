import cv2


image = cv2.imread('g4g.png')
cv2.imshow("Original Image", image) 

# Define the crop coordinates
start_x, end_x = 250, 750  
start_y, end_y = 250, 750 

# Crop the image using slicing
crop_image = image[start_y:end_y, start_x:end_x]

# Display the cropped image
cv2.imshow("Cropped Image", crop_image)

# Save the cropped image as PNG
cv2.imwrite('g4g_cropped.png', crop_image)

# Wait for a key press and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()