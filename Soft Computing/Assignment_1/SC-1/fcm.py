import numpy as np
import pandas as pd
from sklearn import datasets

# Load the Iris dataset
iris = datasets.load_iris()
data = iris.data


def initialize_membership_matrix(n_samples, n_clusters):
    membership_matrix = np.random.rand(n_samples, n_clusters)
    membership_matrix /= np.sum(membership_matrix, axis=1)[:, np.newaxis]
    return membership_matrix


def calculate_cluster_centroids(data, membership_matrix):
    n_clusters = membership_matrix.shape[1]
    centroids = np.zeros((n_clusters, data.shape[1]))
    for j in range(n_clusters):
        # Handle the case where a cluster has no assigned data points
        if np.sum(membership_matrix[:, j]) > 0:
            centroids[j] = np.sum(
                (membership_matrix[:, j] ** 2)[:, np.newaxis] * data, axis=0
            ) / np.sum(membership_matrix[:, j] ** 2)
    return centroids


def update_membership_matrix(data, centroids, m):
    n_samples, n_clusters = data.shape[0], centroids.shape[0]
    membership_matrix = np.zeros((n_samples, n_clusters))

    for i in range(n_samples):
        for j in range(n_clusters):
            numerator = np.linalg.norm(data[i] - centroids[j]) ** 2
            denominator = sum(
                (np.linalg.norm(data[i] - centroids[k]) ** 2) for k in range(n_clusters)
            )
            if denominator == 0:
                # Handle the case where denominator is zero (avoid division by zero)
                membership_matrix[i, j] = 1.0
            else:
                membership_matrix[i, j] = 1.0 / (
                    (numerator / denominator) ** (1.0 / (m - 1))
                )
    membership_matrix /= np.sum(membership_matrix, axis=1)[:, np.newaxis]
    return membership_matrix


def fuzzy_c_means(data, n_clusters, m, max_iterations=100, tolerance=1e-4):
    n_samples = data.shape[0]
    membership_matrix = initialize_membership_matrix(n_samples, n_clusters)

    for iteration in range(max_iterations):
        centroids = calculate_cluster_centroids(data, membership_matrix)
        new_membership_matrix = update_membership_matrix(data, centroids, m)

        # Check for convergence
        if np.max(np.abs(new_membership_matrix - membership_matrix)) < tolerance:
            break

        membership_matrix = new_membership_matrix

    # Display cluster centroids and membership values for each data point
    for j in range(n_clusters):
        print(f"Cluster {j + 1} - Centroid: {centroids[j]}")
        cluster_membership = membership_matrix[:, j]
        for i in range(n_samples):
            print(
                f"Point A{i + 1}: {data[i]} Membership Value = {cluster_membership[i]:.4f}"
            )


if __name__ == "__main__":
    np.random.seed(0)  # For reproducibility
    n_clusters = 3
    m = 2
    print("---IRIS Dataset---")
    print("FOR CLUSTER VALUE 3")
    fuzzy_c_means(data, n_clusters, m)
    n_clusters = 5
    print("FOR CLUSTER VALUE 5")
    fuzzy_c_means(data, n_clusters, m)
    print()
    m = 2
    data = np.array(
        [
            [2, 10],
            [2, 6],
            [11, 11],
            [6, 9],
            [6, 4],
            [1, 2],
            [5, 10],
            [4, 9],
            [10, 12],
            [7, 5],
            [9, 11],
            [4, 6],
            [3, 10],
            [3, 8],
            [6, 11],
        ],
        dtype=float,
    )
    print("---Custom Dataset---")
    print("FOR CLUSTER VALUE 3")
    fuzzy_c_means(data, 3, m)
    print("FOR CLUSTER VALUE 5")
    fuzzy_c_means(data, 5, m)
