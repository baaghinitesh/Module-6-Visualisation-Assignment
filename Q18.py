# 3. Generate a Bokeh bar chart representing the counts of different fruits using the following dataset.
# fruits = ['Apples', 'Oranges', 'Bananas', 'Pears']
# counts = [20, 25, 30, 35]

from bokeh.plotting import figure, show
from bokeh.io import output_notebook


# Dataset
fruits = ['Apples', 'Oranges', 'Bananas', 'Pears']
counts = [20, 25, 30, 35]

# Create a Bokeh figure
p = figure(x_range=fruits, title="Fruit Counts", 
           x_axis_label='Fruits', y_axis_label='Counts', 
           width=800, height=400)

# Add bars to the plot
p.vbar(x=fruits, top=counts, width=0.5, color='blue')

# Show the plot
show(p)
