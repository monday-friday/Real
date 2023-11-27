import cv2, os
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

img_path = 'img/09.jpg'
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# img = cv2.resize(img, dsize=None, fx=0.2, fy=0.2)

# print(img.shape)

plt.figure(figsize=(20, 20))
plt.axis('off')
plt.imshow(img, cmap='gray')


sample_imgs = np.load('dataset/k49-train-imgs.npz')['arr_0']

plt.figure(figsize=(20, 10))
for i in range(80):
    img_patch = 255 - sample_imgs[i]

    plt.subplot(5, 16, i+1)
    plt.title(int(np.mean(img_patch)))
    plt.axis('off')
    plt.imshow(img_patch, cmap='gray')





