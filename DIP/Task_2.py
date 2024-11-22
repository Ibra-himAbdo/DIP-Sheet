import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mpimg.imread('images/g4g.png')
plt.imshow(img)
plt.axis('off') 
plt.show()

#--------------------------
from PIL import Image

img = Image.open('images/g4g.png')

img.show()

print(img.format)

print(img.mode)