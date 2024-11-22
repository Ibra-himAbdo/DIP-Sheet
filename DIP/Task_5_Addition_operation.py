import cv2
import matplotlib.pyplot as plt

tom = cv2.imread('images/jj.png')
jerry = cv2.imread('images/tt.png')

tom = cv2.cvtColor(tom, cv2.COLOR_BGR2RGB)
jerry = cv2.cvtColor(jerry, cv2.COLOR_BGR2RGB)

if tom.shape != jerry.shape:
    jerry = cv2.resize(jerry, (tom.shape[1], tom.shape[0]))

tANDJ = cv2.add(tom, jerry)

plt.figure(figsize=(20, 20))
plt.subplot(1, 3, 1), plt.imshow(tom), plt.title('Tom')
plt.subplot(1, 3, 2), plt.imshow(jerry), plt.title('Jerry')
plt.subplot(1, 3, 3), plt.imshow(tANDJ), plt.title('Tom + Jerry')
plt.show()