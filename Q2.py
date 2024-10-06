# 2. Generate a line plot to visualize the trend of values for the given data.
# data = np.array([3, 7, 9, 15, 22, 29, 35])


import numpy as np
import matplotlib.pyplot as plt

# Given data
data = np.array([3, 7, 9, 15, 22, 29, 35])

# Generate x values based on the length of the data
x = np.arange(len(data))

# Create a line plot
plt.plot(x, data, marker='o', color='blue', linestyle='-')

# Add title and labels
plt.title('Line Plot of Data Values')
plt.xlabel('Index')
plt.ylabel('Values')

# Show grid
plt.grid(True)

# Show the plot
plt.xticks(x)  # Set x-ticks to be the indices
plt.show()
