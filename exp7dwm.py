import numpy as np
import pandas as pd
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as plt

# Step 1: Define the data points and compute the initial distance matrix
data_points = np.array([18, 22, 25, 27, 42, 43]).reshape(-1, 1)
n = len(data_points)

# Initialize the distance matrix
distance_matrix = np.zeros((n, n))

# Fill the distance matrix with Euclidean distances
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = abs(data_points[i] - data_points[j])

# Convert the distance matrix to a DataFrame for better visualization
dist_df = pd.DataFrame(distance_matrix, index=data_points.flatten(), columns=data_points.flatten())
print("Initial Distance Matrix:")
print(dist_df)

# Step 2: Perform Agglomerative Clustering with single linkage and show step-by-step process
clusters = [[point[0]] for point in data_points]  # Initialize clusters with each data point
print("\nInitial Clusters:", clusters)

# Helper function to calculate single linkage distance between clusters
def single_linkage_distance(cluster1, cluster2, distance_matrix):
    min_dist = np.inf
    for point1 in cluster1:
        for point2 in cluster2:
            dist = distance_matrix[data_points.flatten() == point1, data_points.flatten() == point2][0]
            if dist < min_dist:
                min_dist = dist
    return min_dist

# Iteratively merge clusters
while len(clusters) > 1:
    # Find the two closest clusters
    min_distance = np.inf
    cluster_to_merge = (None, None)

    # Display the current distance matrix
    print("\nCurrent Distance Matrix:")
    dist_matrix = np.zeros((len(clusters), len(clusters)))
    
    for i in range(len(clusters)):
        for j in range(i + 1, len(clusters)):
            dist = single_linkage_distance(clusters[i], clusters[j], distance_matrix)
            dist_matrix[i, j] = dist
            dist_matrix[j, i] = dist
            if dist < min_distance:
                min_distance = dist
                cluster_to_merge = (i, j)

    dist_df = pd.DataFrame(dist_matrix)
    print(dist_df)
    
    # Merge the two closest clusters
    cluster1, cluster2 = cluster_to_merge
    new_cluster = clusters[cluster1] + clusters[cluster2]
    clusters.append(new_cluster)

    # Remove old clusters
    clusters.pop(max(cluster1, cluster2))
    clusters.pop(min(cluster1, cluster2))

    print(f"\nMerged clusters {cluster1} and {cluster2} with distance {min_distance}")
    print("Updated Clusters:", clusters)

# Step 3: Calculate the linkage matrix and plot the dendrogram
linked = sch.linkage(data_points, method='single')

plt.figure(figsize=(10, 7))
dendrogram = sch.dendrogram(linked, labels=[18, 22, 25, 27, 42, 43])

plt.title("Agglomerative Clustering Dendrogram (Single Linkage)")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()
