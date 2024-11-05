import numpy as np

def kmeans(data, initial_centroids, iterations=100):
    centroids = initial_centroids.copy()
    print(f"Initial Centroids: {centroids.flatten()}")
    
    for iteration in range(iterations):
        labels = np.argmin(np.linalg.norm(data[:, np.newaxis] - centroids, axis=2), axis=1)
        new_centroids = np.array([data[labels == i].mean(axis=0) for i in range(len(centroids))])
        
        print(f"\nIteration {iteration + 1}:")
        for i in range(len(new_centroids)):
            print(f"Cluster {i + 1}: {data[labels == i].flatten()}")
        print("New Centroids:", new_centroids.flatten())
        
        if np.array_equal(centroids, new_centroids):
            break
        centroids = new_centroids

    return labels, centroids

# User input
print("Joan Zachariah, TE CMPN B , 61")
data = np.array([float(x) for x in input("Enter an array of numbers separated by spaces: ").split()]).reshape(-1, 1)
initial_centroids = np.array([float(x) for x in input(f"Enter {int(input('Enter the number of clusters: '))} initial centroids separated by spaces: ").split()]).reshape(-1, 1)

# Run K-Means
labels, final_centroids = kmeans(data, initial_centroids)

# Final output
print("\nFinal Clusters:")
for i in range(len(final_centroids)):
    print(f"Cluster {i + 1}: {data[labels == i].flatten()}")
print("Final Centroids:", final_centroids.flatten())