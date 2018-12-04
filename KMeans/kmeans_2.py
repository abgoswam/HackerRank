import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def display_plot(observations, associated_centroids, loc_centroics):
    assert len(observations) == len(associated_centroids)

    colors = ['r', 'g', 'b', 'y', 'c', 'm']
    for k in range(K):
        obs_k = observations[associated_centroids == k, :]
        obs_kx = obs_k[:, 0]
        obs_ky = obs_k[:, 1]
        plt.scatter(obs_kx, obs_ky, c=colors[k])

    plt.scatter(loc_centroics[:, 0], loc_centroics[:, 1], s=200, marker='*')
    plt.show()


# Data exploration

data = pd.read_csv('xclara.csv')
print(data.head())
print(data.shape)

V1_min = np.min(data['V1'])
V1_max = np.max(data['V1'])
V2_min = np.min(data['V2'])
V2_max = np.max(data['V2'])
nobs, ndims = data.shape

plt.scatter(data['V1'], data['V2'])
plt.show()

# data points
obs = data.values

# initialize K centroid
K = 5
rx = np.random.uniform(V1_min, V1_max, size=(K, 1))
ry = np.random.uniform(V2_min, V2_max, size=(K, 1))
rcentroids = np.hstack((rx, ry))

closest_centroids = np.zeros(nobs)

for _ in range(2):
    for i in range(nobs):
        o = obs[i]
        o_centroid_dist = np.linalg.norm(o-rcentroids, axis=1)
        o_centroid_closest = np.argmin(o_centroid_dist)
        closest_centroids[i] = o_centroid_closest

    display_plot(obs, closest_centroids, rcentroids)

    for k in range(K):
        obs_k = obs[closest_centroids == k, :]
        if len(obs_k) > 0:
            rcentroids[k] = obs_k.mean(axis=0)

    display_plot(obs, closest_centroids, rcentroids)








