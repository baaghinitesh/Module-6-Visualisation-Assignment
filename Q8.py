# 3. Create a dataset representing categories and their corresponding values. Compare different categories based on numerical values.


import matplotlib.pyplot as plt

# Define categories and their corresponding values
categories = ['Category A', 'Category B', 'Category C', 'Category D', 'Category E']
values = [35, 50, 25, 40, 60]

# Create a bar chart
plt.figure(figsize=(10, 6))  # Optional: set figure size
plt.bar(categories, values, color='lightblue', edgecolor='black')

# Add title and labels
plt.title('Comparison of Categories Based on Numerical Values')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show grid for better readability
plt.grid(axis='y')

# Display the plot
plt.show()
