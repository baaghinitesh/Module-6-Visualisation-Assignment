# 3. Display a bar chart to represent the frequency of each item in the given array categories.
# categories = ['A', 'B', 'C', 'D', 'E'] values [25, 40, 30, 35, 20]

import matplotlib.pyplot as plt

# Given categories and values
categories = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 35, 20]

# Create a bar chart
plt.bar(categories, values, color='skyblue')

# Add title and labels
plt.title('Frequency of Categories')
plt.xlabel('Categories')
plt.ylabel('Values')

# Show grid for better readability
plt.grid(axis='y')

# Display the plot
plt.show()

