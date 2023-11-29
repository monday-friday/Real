import cv2, os
import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict

from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin_min
from sklearn.utils import shuffle


img_path = 'img_01.jpg'
img = cv2.imread(img_path)

img = cv2.resize(img, dsize=None, fx=0.2, fy=0.2)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(img.shape)

plt.figure(figsize=(20, 20))
plt.axis('off')
plt.imshow(img)

def unpickle(file):
    import pickle
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
        
    data = dict[b'data'].reshape((-1, 3, 32, 32)).transpose(0, 2, 3, 1).astype(np.float64) / 255.

    return data

x_train_1 = unpickle('dataset/data_batch_1')
x_train_2 = unpickle('dataset/data_batch_2')
x_train_3 = unpickle('dataset/data_batch_3')
x_train_4 = unpickle('dataset/data_batch_4')
x_train_5 = unpickle('dataset/data_batch_5')

sample_imgs = np.concatenate([x_train_1, x_train_2, x_train_3, x_train_4, x_train_5], axis=0)

print(sample_imgs.shape)

plt.figure(figsize=(20, 10))
for i in range(80):
    img_patch = sample_imgs[i]

    plt.subplot(5, 16, i+1)
    plt.axis('off')
    plt.imshow(img_patch)

N_CLUSTERS = 32

h, w, d = img.shape

img_array = img.copy().astype(np.float64) / 255.
img_array = np.reshape(img_array, (w * h, d))

# all pixels
img_array_sample = shuffle(img_array, random_state=0)

# pick random 1000 pixels if want to run faster
# img_array_sample = shuffle(img_array, random_state=0)[:1000]

# KMeans clustering
kmeans = KMeans(n_clusters=N_CLUSTERS, random_state=0).fit(img_array_sample)

print(kmeans.cluster_centers_)


cluster_centers = kmeans.cluster_centers_

pred_labels = kmeans.predict(img_array)
cluster_labels = pred_labels.reshape((h, w))

img_quantized = np.zeros((h, w, d), dtype=np.float64)

label_idx = 0
for y in range(h):
    for x in range(w):
        label = pred_labels[label_idx]

        img_quantized[y, x] = cluster_centers[label]

        label_idx += 1

plt.figure(figsize=(20, 20))
plt.axis('off')
plt.imshow(img_quantized)


DISTANCE_THRESHOLD = 0.1

bins = defaultdict(list)

for img_patch in sample_imgs:
    mean = np.mean(img_patch, axis=(0, 1))

    # compare patch mean and cluster centers
    cluster_idx, distance = pairwise_distances_argmin_min(cluster_centers, [mean], axis=0)
    
    if distance < DISTANCE_THRESHOLD:
        bins[cluster_idx[0]].append(img_patch)

# number of bins must equal to N_CLUSTERS. if not, increase DISTANCE_THRESHOLD
assert(len(bins) == N_CLUSTERS)

img_out = np.zeros((h*32, w*32, d), dtype=np.float64)

for y in range(h):
    for x in range(w):
        label = cluster_labels[y, x]

        b = bins[label]

        img_patch = b[np.random.randint(len(b))]

        img_out[y*32:(y+1)*32, x*32:(x+1)*32] = img_patch
        
plt.figure(figsize=(20, 20))
plt.axis('off')
plt.imshow(img_out)

img_out2 = cv2.cvtColor((img_out * 255).astype(np.uint8), cv2.COLOR_RGB2BGR)
_ = cv2.imwrite('result/%s_color.jpg' % os.path.splitext(os.path.basename(img_path))[0], img_out2)

plt.show()









