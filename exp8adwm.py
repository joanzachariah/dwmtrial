import numpy as np

# Define and sort the input array
data = np.array([11, 2, 13, 4, 25, 26, 7, 18, 9])
sorted_data = np.sort(data)

# Number of elements in each bin
bin_size = 3
num_bins = len(sorted_data) // bin_size

# Initialize arrays for means, boundaries, and medians
bin_means = np.zeros(num_bins)
bin_boundaries = np.zeros((num_bins, bin_size))
bin_medians = np.zeros(num_bins)

print("Input Array:\n", data)
print("\nInitial Bins (Subarrays):")

for i in range(num_bins):
    bin_data = sorted_data[i * bin_size:(i + 1) * bin_size]
    print(f"Bin {i + 1}: {bin_data}")

    # Calculate statistics
    bin_means[i] = np.mean(bin_data)
    min_value, max_value = bin_data[0], bin_data[-1]
    
    # Assign boundaries: min, max (repeated to fill bin size)
    bin_boundaries[i] = [min_value] + [max_value] * (bin_size - 1)
    bin_medians[i] = np.median(bin_data)

# Print results
print("\nBin Mean:\n", bin_means.reshape(-1, 1))
print("\nBin Boundaries:\n", bin_boundaries)
print("\nBin Median:\n", bin_medians.reshape(-1, 1))