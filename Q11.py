# 1. Using the given dataset, to generate a 3D scatter plot to visualize the distribution of data points in a three- dimensional space.
# np.random.seed(30)
# data = {
# }
# 'X': np.random. uniform (-10, 10, 300),
# 'Y': np.random. uniform (-10, 10, 300),
# 'Z': np.random. uniform (-10, 10, 300)
# df = pd.DataFrame(data)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Set a random seed for reproducibility
np.random.seed(30)

# Generate the dataset
data = {
    'X': np.random.uniform(-10, 10, 300),
    'Y': np.random.uniform(-10, 10, 300),
    'Z': np.random.uniform(-10, 10, 300)
}
df = pd.DataFrame(data)

# Create a 3D scatter plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(df['X'], df['Y'], df['Z'], color='blue', alpha=0.6)

# Add title and labels
ax.set_title('3D Scatter Plot of Randomly Generated Data')
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Display the plot
plt.show()
