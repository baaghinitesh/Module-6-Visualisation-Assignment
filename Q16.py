# 1.Create a Bokeh plot displaying a sine wave. Set x-values from 0 to 10 and y-values as the sine of x.

import numpy as np
from bokeh.plotting import figure, show

# Generate the x-values and corresponding y-values (sine of x)
x = np.linspace(0, 10, 100)  # 100 points from 0 to 10
y = np.sin(x)

# Create a Bokeh figure
p = figure(title="Sine Wave", x_axis_label='X', y_axis_label='sin(X)', width=800, height=400)

# Add the sine wave to the plot
p.line(x, y, line_width=2, color='blue', legend_label='sin(x)')

# Customize legend
p.legend.location = "top_left"

# Show the plot
show(p)
