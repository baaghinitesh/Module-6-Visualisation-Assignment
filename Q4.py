# 4. Create a histogram to visualize the distribution of values in the array data.
# data= np.random.normal(0, 1, 1000)

import numpy as np
import matplotlib.pyplot as plt

# Generate data from a normal distribution
data = np.random.normal(0, 1, 1000)

# Create a histogram
plt.hist(data, bins=30, color='skyblue', edgecolor='black')

# Add title and labels
plt.title('Histogram of Normally Distributed Data')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show grid for better readability
plt.grid(axis='y')

# Display the plot
plt.show()

