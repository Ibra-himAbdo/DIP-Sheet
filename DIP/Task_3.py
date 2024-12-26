import cv2
from PIL import Image

# OpenCV Color Image
im = cv2.imread('images/lena.jpg')  # Replace with your image file

# Check type of image
print("Type of image:", type(im))

# Color Image - Shape and Dimensions
print("\nColor Image Shape:")
print("im.shape:", im.shape)
print("Type of shape:", type(im.shape))

# Unpacking tuple for color image
h, w, c = im.shape
print('Width:  ', w)
print('Height: ', h)
print('Channel:', c)

# Alternative unpacking method
h, w, _ = im.shape
print('Width: ', w)
print('Height:', h)

# Accessing by index
print('Width: ', im.shape[1])
print('Height:', im.shape[0])

# OpenCV Grayscale Image
im_gray = cv2.imread('images/lena.jpg', cv2.IMREAD_GRAYSCALE)

# Grayscale Image - Shape and Dimensions
print("\nGrayscale Image Shape:")
print("im_gray.shape:", im_gray.shape)
print("Type of shape:", type(im_gray.shape))

# Unpacking tuple for grayscale image
h, w = im_gray.shape
print('Width: ', w)
print('Height:', h)

# Accessing by index for grayscale
print('Width: ', im_gray.shape[1])
print('Height:', im_gray.shape[0])

# Pillow (PIL) Image
from PIL import Image

im_pil = Image.open('images/lena.jpg')

# PIL Image Size
print("\nPIL Image Size:")
print("im.size:", im_pil.size)
print("Type of size:", type(im_pil.size))

# Unpacking PIL size
w, h = im_pil.size
print('Width: ', w)
print('Height:', h)

# Using width and height attributes
print('Width: ', im_pil.width)
print('Height:', im_pil.height)

# Additional Image Information
print("\nAdditional Image Information:")
print('Image Data Type:', im.dtype)
print('Minimum Pixel Value:', im.min())
print('Maximum Pixel Value:', im.max())
print('Total Pixels:', im.size)