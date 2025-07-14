import numpy as np
from scipy.cluster.vq import kmeans, whiten
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid")

pts = 10
rands = np.random.randint(0, 100, (10, 2))
# Generate two clusters of points
print(rands)
a = np.random.multivariate_normal([0, 0], [[1, 0], [0, 1]], pts)
b = np.random.multivariate_normal([5, 5], [[1, 0], [0, 1]], pts)

features = np.concatenate((a, b), axis=0)

whitened_features = whiten(features)

codebook = kmeans(whitened_features, 2)

plt.scatter(features[:, 0], features[:, 1], c='blue', label='Data Points')
plt.scatter(codebook[0][:, 0], codebook[0][:, 1], c='red', marker='x', s=100, label='Centroids')
plt.show()