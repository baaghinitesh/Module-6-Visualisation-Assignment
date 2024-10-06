# 5. Using the given dataset, create a bubble chart to represent each country's population (y-axis), GDP (x- axis), and bubble size proportional to the population.
# np.random.seed(25)
# data = {
# 'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
# 'Population':
# np.random.randint (100, 1000, 5),
# 5)
# }
# 'GDP' np.random.randint(500, 2000,
# df = pd.DataFrame(data)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Set a random seed for reproducibility
np.random.seed(25)

# Generate the dataset
data = {
    'Country': ['USA', 'Canada', 'UK', 'Germany', 'France'],
    'Population': np.random.randint(100, 1000, 5),
    'GDP': np.random.randint(500, 2000, 5)
}
df = pd.DataFrame(data)

# Create a bubble chart
plt.figure(figsize=(10, 6))
plt.scatter(df['GDP'], df['Population'], s=df['Population']*10, alpha=0.5, c='blue', edgecolors='w', linewidth=2)

# Add labels and title
for i, country in enumerate(df['Country']):
    plt.annotate(country, (df['GDP'][i], df['Population'][i]), fontsize=10, ha='right')

plt.title('Bubble Chart of Population vs GDP by Country')
plt.xlabel('GDP (in billions)')
plt.ylabel('Population (in millions)')

# Display the plot
plt.grid()
plt.show()

