import math
import numpy as np
from sklearn import datasets

# Function to calculate the Euclidean distance between two points


def euclidean_distance(point1, point2):
    distance = 0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i])**2
    return math.sqrt(distance)

# Implement K-Means


def k_means(data, k):
    # Initialize the centroids
    centroids = []
    for i in range(k):
        centroids.append(data[i])

    # Iterate until the centroids no longer change
    while True:
        # Assign each data point to the cluster with the closest centroid
        clusters = [[] for i in range(k)]
        for point in data:
            closest_centroid = None
            closest_distance = float("inf")
            for i, centroid in enumerate(centroids):
                distance = euclidean_distance(point, centroid)
                if distance < closest_distance:
                    closest_centroid = i
                    closest_distance = distance
            clusters[closest_centroid].append(point)

        # Update the centroids
        new_centroids = []
        for i in range(k):
            new_centroids.append(np.mean(clusters[i], axis=0))

        # Check if the centroids have changed
        if np.array_equal(centroids, new_centroids):
            break

        centroids = new_centroids

    # Print centroid and the clusters associated with that centroid
    for i, centroid in enumerate(centroids):
        print(f"Centroid {i+1}: {centroid}")
        for point in clusters[i]:
            print(point)


print("---Iris Dataset---")
iris = datasets.load_iris()
points = iris.data
print("No.of Clusters: 2")
k_means(points, 2)
print("No.of Clusters: 4")
k_means(points, 4)
print()
print("---Custom Dataset---")
points = np.array([[2, 10], [2, 6], [11, 11], [6, 9], [6, 4], [1, 2], [5, 10], [
                  4, 9], [10, 12], [7, 5], [9, 11], [4, 6], [3, 10], [3, 8], [6, 11]])
print("No.of Clusters: 2")
k_means(points, 2)
print("No.of Clusters: 4")
k_means(points, 4)
