# 4. Generate a dataset with categories and numerical values. Visualize the distribution of a numerical variable across different categories.

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Generate a dataset
np.random.seed(42)  # For reproducibility
categories = ['Category A', 'Category B', 'Category C']
data = {
    'Category': np.random.choice(categories, size=300),  # Randomly assign categories
    'Value': np.random.normal(loc=50, scale=10, size=300)  # Random values with normal distribution
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a box plot to visualize the distribution of values across categories
plt.figure(figsize=(10, 6))
df.boxplot(column='Value', by='Category', grid=False)

# Add title and labels
plt.title('Distribution of Values Across Categories')
plt.suptitle('')  # Suppress the default title to keep it clean
plt.xlabel('Categories')
plt.ylabel('Values')

# Display the plot
plt.show()
