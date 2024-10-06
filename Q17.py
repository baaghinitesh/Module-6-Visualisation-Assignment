# 2.Create a Bokeh scatter plot using randomly generated x and y values. Use different sizes and colors for the markers based on the 'sizes' and 'colors' columns.

import numpy as np
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

# Generate random data
np.random.seed(42)  # For reproducibility
n = 100  # Number of points
x = np.random.rand(n) * 100  # Random x values
y = np.random.rand(n) * 100  # Random y values
sizes = np.random.randint(5, 50, size=n)  # Random sizes for the markers
colors = np.random.choice(['red', 'green', 'blue', 'orange', 'purple'], size=n)  # Random colors

# Create a DataFrame (optional, for better data handling)
data = {
    'x': x,
    'y': y,
    'sizes': sizes,
    'colors': colors
}
df = pd.DataFrame(data)

# Create a scatter plot
p = figure(title="Random Scatter Plot", x_axis_label='X', y_axis_label='Y', width=800, height=400)

# Add scatter points to the plot
p.scatter('x', 'y', size='sizes', color='colors', source=df, alpha=0.6)

# Show the plot
show(p)
