# 2. Generate a dataset of random numbers. Visualize the distribution of a numerical variable.

import numpy as np
import matplotlib.pyplot as plt

# Generate a dataset of random numbers from a normal distribution
np.random.seed(42)  # For reproducibility
data = np.random.normal(loc=50, scale=10, size=1000)  # mean = 50, std = 10, n = 1000

# Create a histogram to visualize the distribution
plt.figure(figsize=(10, 6))  # Optional: set figure size
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)

# Add title and labels
plt.title('Distribution of Random Numbers')
plt.xlabel('Value')
plt.ylabel('Frequency')

# Show grid for better readability
plt.grid(axis='y')

# Display the plot
plt.show()
