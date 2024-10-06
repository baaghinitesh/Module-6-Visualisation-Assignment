# 1. Create a scatter plot to visualize the relationship between two variables, by generating a synthetic dataset.

import numpy as np
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(42)

# Generate synthetic data
# Independent variable (x)
x = np.linspace(0, 10, 100)

# Dependent variable (y) with some noise
# Here y is linearly related to x with some random noise
y = 2 * x + 5 + np.random.normal(0, 2, size=x.shape)

# Create a scatter plot
plt.scatter(x, y, color='blue', marker='o', label='Data points')

# Add a line of best fit
m, b = np.polyfit(x, y, 1)  # Linear fit
plt.plot(x, m*x + b, color='red', label='Line of Best Fit')

# Add title and labels
plt.title('Scatter Plot of Synthetic Dataset')
plt.xlabel('Independent Variable (x)')
plt.ylabel('Dependent Variable (y)')

# Show legend
plt.legend()

# Show grid for better readability
plt.grid(True)

# Display the plot
plt.show()
