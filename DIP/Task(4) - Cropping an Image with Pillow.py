from PIL import Image

# Load the image
img = Image.open('g4g.png')  
img.show() 


box = (250, 250, 750, 750)


img_cropped = img.crop(box)


if img_cropped.mode == 'RGBA':
    img_cropped = img_cropped.convert('RGB')

# Save the cropped image as JPEG
img_cropped.save('g4g_cropped.jpg', 'JPEG')

# Display the cropped image
img_cropped.show()