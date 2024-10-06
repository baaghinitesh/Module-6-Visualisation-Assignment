# 5. Generate a synthetic dataset with correlated features. Visualize the correlation matrix of a dataset using a heatmap.

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(42)

# Generate a synthetic dataset with correlated features
n_samples = 100
x1 = np.random.normal(0, 1, n_samples)  # Feature 1
x2 = x1 * 0.5 + np.random.normal(0, 0.5, n_samples)  # Feature 2, correlated with Feature 1
x3 = x1 * 0.2 + np.random.normal(0, 0.5, n_samples)  # Feature 3, less correlated
x4 = np.random.normal(0, 1, n_samples)  # Feature 4, independent

# Combine features into a DataFrame
data = pd.DataFrame({'Feature 1': x1, 'Feature 2': x2, 'Feature 3': x3, 'Feature 4': x4})

# Calculate the correlation matrix
correlation_matrix = data.corr()

# Create a heatmap to visualize the correlation matrix
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f', square=True, linewidths=0.5)

# Add title
plt.title('Correlation Matrix Heatmap')

# Display the plot
plt.show()
