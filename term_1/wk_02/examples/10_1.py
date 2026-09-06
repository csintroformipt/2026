from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import grid
import numpy as np

output_file("lines_and_scatters.html")


x = np.linspace(-4, 4, 1000)

def func_lin(x):
    return 2*x

def func_square(x):
    return x*x

def func_sign(x):
    if x < 0:
        return -1
    elif x > 0:
        return 1
    else:
        return 0
    
y_lin = func_lin(x)
y_square = func_square(x)

#y_sign =  func_sign(x) #causes error
y_sign =  np.vectorize(func_sign)(x)

p = figure(width=400, height=400)
p.line(x, y_lin, color='red', legend_label="lin")
p.line(x, y_square, color='blue', legend_label="square")
p.line(x, y_sign, color='green', legend_label="signum")

from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

cds = ColumnDataSource(data = {'x':x, 'y_lin':y_lin, 'y_square':y_square, 'y_sign':y_sign})

p.scatter(x='x', y='y_lin', source=cds, marker="circle", size = 1, color = "purple", legend_label="sc_lin")
p.scatter(x='x', y='y_square', source=cds, marker="square", size = 2, color = "orange", legend_label="sc_square")
p.scatter(x='x', y='y_sign', source=cds, marker="triangle", size = 3, color = "cyan", legend_label="sc_signum")

p.legend.location = "top_left"
p.legend.click_policy="hide"

show(grid(p, sizing_mode="stretch_both"))