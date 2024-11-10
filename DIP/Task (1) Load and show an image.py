import cv2

img = cv2.imread('g4g.png',1)
# 1 --> unchange
image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('image', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
