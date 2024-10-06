# 5. Create a Bokeh heatmap using the provided dataset.
# data_heatmap = np.random.rand(10, 10)
# x = np.linspace (0, 1, 10)
# y= np.linspace (0, 1, 10)
# xx, yy = np.meshgrid(x, y)


import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook
from bokeh.transform import linear_cmap
from bokeh.models import ColorBar
from bokeh.palettes import Viridis256  # Use the palette directly

# Optional: If you're using a Jupyter notebook, uncomment the line below
# output_notebook()

# Generate random data for the heatmap
data_heatmap = np.random.rand(10, 10)

# Define x and y ranges
x = np.linspace(0, 1, 10)
y = np.linspace(0, 1, 10)
xx, yy = np.meshgrid(x, y)

# Prepare data for Bokeh
heatmap_data = {
    'x': xx.flatten(),
    'y': yy.flatten(),
    'value': data_heatmap.flatten()
}

# Create a Bokeh figure
p = figure(title="Heatmap", 
           x_axis_label='X', 
           y_axis_label='Y', 
           width=600, height=600)

# Create a color mapper
mapper = linear_cmap(field_name='value', palette=Viridis256, low=min(heatmap_data['value']), high=max(heatmap_data['value']))

# Add rectangles to the heatmap
p.rect(x='x', y='y', width=0.1, height=0.1, source=heatmap_data, line_color=None, fill_color=mapper)

# Add a color bar
color_bar = ColorBar(color_mapper=mapper['transform'], location=(0, 0))
p.add_layout(color_bar, 'right')

# Show the plot
show(p)
