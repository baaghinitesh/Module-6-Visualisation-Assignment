# 3. Using the sales data, generate a heatmap to visualize the variation in sales across different months and days.
# np.random.seed(20)
# data = {
# }
# 'Month' np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
# 'Day' np.random.choice (range(1, 31), 100),
# 'Sales': np.random.randint(1000, 5000, 100)
# df = pd.DataFrame(data)


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(20)

# Generate the dataset for sales data
data = {
    'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
    'Day': np.random.choice(range(1, 31), 100),
    'Sales': np.random.randint(1000, 5000, 100)
}
df = pd.DataFrame(data)

# Create a pivot table for the heatmap
pivot_table = df.pivot_table(values='Sales', index='Day', columns='Month', aggfunc='mean', fill_value=0)

# Create a heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='.0f')

# Add title and labels
plt.title('Heatmap of Sales Variation Across Months and Days')
plt.xlabel('Month')
plt.ylabel('Day')

# Display the plot
plt.show()
