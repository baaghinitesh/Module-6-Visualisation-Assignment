# 4. Using the given x and y data, generate a 3D surface plot to visualize the function z = sin(√x2 + y2
# x = np.linspace (-5, 5, 100)
# y = np.linspace(-5, 5, 100) x, y = np.meshgrid(x, y)
# z = np.sin(np.sqrt(x**2 + y**2))
# data = {
# }
# 'X': x.flatten(),
# 'Y' y.flatten(),
# 'Z' z.flatten()
# df = pd.DataFrame(data)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Generate the x and y data
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# Calculate z based on the function
z = np.sin(np.sqrt(x**2 + y**2))

# Prepare the data for DataFrame (optional)
data = {
    'X': x.flatten(),
    'Y': y.flatten(),
    'Z': z.flatten()
}
df = pd.DataFrame(data)

# Create a 3D surface plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(x, y, z, cmap='viridis', edgecolor='none')

# Add title and labels
ax.set_title('3D Surface Plot of z = sin(√(x² + y²))')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')

# Add a color bar
fig.colorbar(surf)

# Display the plot
plt.show()

