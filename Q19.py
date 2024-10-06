# 4. Create a Bokeh histogram to visualize the distribution of the given data.
# data_hist= np.random.randn(1000)
# hist, edges = np.histogram (data_hist, bins=30)

import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

# Optional: If you're using a Jupyter notebook, uncomment the line below
# output_notebook()

# Generate random data
data_hist = np.random.randn(1000)

# Calculate histogram
hist, edges = np.histogram(data_hist, bins=30)

# Create a Bokeh figure
p = figure(title="Histogram of Normally Distributed Data", 
           x_axis_label='Value', 
           y_axis_label='Frequency', 
           width=800, height=400)

# Add the histogram bars
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:], fill_color='blue', line_color='black')

# Show the plot
show(p)

