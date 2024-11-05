import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data into a DataFrame and clean column names
data_df = pd.read_csv(r"exp8b.csv").rename(columns=lambda x: x.strip())

# Print cleaned column names to verify
print("Available columns in the CSV file:\n", data_df.columns)

# Extract data for plotting
hist_data = data_df['Height']
scatter_x = data_df['Height']
scatter_y = data_df['Age']

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 7))

# Plot histogram
ax1.hist(hist_data, bins=30, color='skyblue', edgecolor='black')
ax1.set(title='Histogram of Height', xlabel='Height', ylabel='Frequency')

# Plot scatter plot
ax2.scatter(scatter_x, scatter_y, color='orange')
ax2.set(title='Scatter Plot of Height vs Age', xlabel='Height', ylabel='Age')

# Adjust layout and show the plot
plt.tight_layout()
plt.show()