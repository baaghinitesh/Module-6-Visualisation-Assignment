# 2. Using the Student Grades, create a violin plot to display the distribution of scores across different grade categories.
# np.random.seed(15)
# data = {
# }
# 'Grade'
# np.random. choice (['A', 'B', 'C', 'D', 'F'], 200),
# 'Score': np.random.randint(50, 100, 200)
# df = pd.DataFrame(data)
# 1. Using the sales data, generate a heatmap to visualize the variation in sales across different         months and days.
# np.random.seed(20)
# data = {
# }
# 'Month' np.random.choice (['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
# 'Day' np.random.choice (range(1, 31), 100),
# 'Sales' np.random.randint(1000, 5000, 100)
# df = pd.DataFrame(data)

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(15)

# Generate the dataset for student grades and scores
grade_data = {
    'Grade': np.random.choice(['A', 'B', 'C', 'D', 'F'], 200),
    'Score': np.random.randint(50, 100, 200)
}
grades_df = pd.DataFrame(grade_data)

# Create a violin plot for student grades
plt.figure(figsize=(12, 6))

# Violin Plot
plt.subplot(1, 2, 1)  # Create a subplot for the violin plot
sns.violinplot(x='Grade', y='Score', data=grades_df, inner='quartile', hue='Grade', palette='muted', legend=False)
plt.title('Distribution of Scores Across Different Grade Categories')
plt.xlabel('Grade')
plt.ylabel('Score')

# Set a random seed for sales data
np.random.seed(20)

# Generate the dataset for sales data
sales_data = {
    'Month': np.random.choice(['Jan', 'Feb', 'Mar', 'Apr', 'May'], 100),
    'Day': np.random.choice(range(1, 31), 100),
    'Sales': np.random.randint(1000, 5000, 100)
}
sales_df = pd.DataFrame(sales_data)

# Create a pivot table for the heatmap
pivot_table = sales_df.pivot_table(values='Sales', index='Day', columns='Month', aggfunc='mean', fill_value=0)

# Heatmap
plt.subplot(1, 2, 2)  # Create a subplot for the heatmap
sns.heatmap(pivot_table, cmap='YlGnBu', annot=True, fmt='.0f')
plt.title('Heatmap of Sales Variation Across Months and Days')
plt.xlabel('Month')
plt.ylabel('Day')

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
