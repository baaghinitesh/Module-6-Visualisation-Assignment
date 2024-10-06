# 5. Show a pie chart to represent the percentage distribution of different sections in the array`sections`. sections = ['Section A', 'Section B', 'Section C', 'Section D']
# sizes = [25, 30, 15, 30]

import matplotlib.pyplot as plt

# Given sections and sizes
sections = ['Section A', 'Section B', 'Section C', 'Section D']
sizes = [25, 30, 15, 30]

# Create a pie chart
plt.figure(figsize=(8, 6))  # Optional: set figure size
plt.pie(sizes, labels=sections, autopct='%1.1f%%', startangle=140)

# Add title
plt.title('Percentage Distribution of Sections')

# Equal aspect ratio ensures that pie chart is a circle
plt.axis('equal')

# Display the plot
plt.show()
