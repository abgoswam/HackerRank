import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def euclidean_distance(a, b):
    return np.linalg.norm(a - b)


data = pd.read_csv('xclara.csv')

print(data.head())
print(data.shape)

# Getting the values and plotting it
# f1 = data['V1'].values
# f2 = data['V2'].values
X = data.values
plt.scatter(X[:, 0], X[:, 1], c='black', s=1)
plt.show()

# Number of clusters
k = 5
# # X coordinates of random centroids
# C_x = np.random.randint(0, np.max(X) - 20, size=k)
# # Y coordinates of random centroids
# C_y = np.random.randint(0, np.max(X) - 20, size=k)
# C = np.array(list(zip(C_x, C_y)), dtype=np.float32)
C = np.random.randint(0, np.max(X)-20, size=(k, 2))
print("C:{0}".format(C))
plt.scatter(X[:, 0], X[:, 1], c='black', s=1)
plt.scatter(C[:, 0], C[:, 1], c='g', s=200, marker='*')
plt.show()

# Cluster Lables(0, 1, 2)
clusters = np.zeros(len(X))

while True:
    C_new = np.zeros((k, 2))
    count = np.zeros(k)
    # Find distance of each point from cluster centroids
    for i in range(len(X)):
        dist = np.zeros(k)
        for c in range(k):
            dist[c] = euclidean_distance(X[i], C[c])

        ic = np.argmin(dist)

        count[ic] += 1
        C_new[ic] += X[i]
        clusters[i] = ic

    for c in range(k):
        C_new[c] /= count[c]

    if euclidean_distance(C, C_new) < 0.0001:
        break
    else:
        C = C_new

print("C_new:{0}".format(C_new))
plt.scatter(X[:, 0], X[:, 1], c='black', s=1)
plt.scatter(C_new[:, 0], C_new[:, 1], c='blue', s=200)
plt.show()

colors = ['r', 'g', 'b', 'y', 'c', 'm']
fig, ax = plt.subplots()
for i in range(k):
        points = np.array([X[j] for j in range(len(X)) if clusters[j] == i])
        ax.scatter(points[:, 0], points[:, 1], s=7, c=colors[i])
ax.scatter(C[:, 0], C[:, 1], marker='*', s=200, c='#050505')
plt.show()
