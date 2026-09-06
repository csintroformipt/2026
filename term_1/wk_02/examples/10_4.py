#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 12:04:28 2019

@author: dilis
"""
import argparse
import numpy as np

class Poly:
    def __init__(self):
        self.max_order = 20
        self.alph = np.zeros(self.max_order)
        self.order = 0
        
    
    def set_poly(self, a_vec):
        if len(a_vec) >= self.max_order:
            print("Warning: the order is too big. Using first {} elements from it".format(self.max_order))
        self.order = np.min([self.max_order, len(a_vec)])
        print("Initializing Polynom of order <{}".format(self.order))
        self.alph[:self.order] = a_vec[:self.order]
        self.print_poly()
     
    def update_poly_text(self):
        self.poly_text = ""
        for idx, ai in enumerate(self.alph[:self.order]):
            self.poly_text = self.poly_text + "+ ({}) * x^{} ".format(ai, idx)
        
    def print_poly(self):
        self.update_poly_text()
        print (self.poly_text)
            
    def ev(self, x):
        val = 0.0
        for ai in self.alph[self.order::-1]:
            val = ai + val * x
        return val
    
    def evd(self, x):
        val = 0.0
        for idx, ai in enumerate(self.alph[self.order:0:-1]):
            val = (self.order-idx)*ai + val * x
        return val
    
    def get_root(self, x0, tol):
        tolerance = tol**2
        x = x0
        fx = self.ev(x)
        res = np.abs(fx)**2
        
        if (res < tolerance):
                return x
        for i in range(100):
            x = x - fx / self.evd(x)
            fx = self.ev(x)
            res = np.abs(fx)**2
            if (res < tolerance):
                return x
        print ("Unconverged for x0={}".format(x0))
        return np.nan + np.nan*1j # max iteration_count reached
    
def gen_figure(roots):
    data = np.real(roots)
    from bokeh.io import output_file, show
    from bokeh.plotting import figure
    from bokeh.models import LinearColorMapper, BasicTicker, ColorBar
    from bokeh.layouts import layout, row
        
    TOOLS = "crosshair,pan,wheel_zoom,box_zoom,reset,save,box_select,lasso_select,tap,hover"
    TOOLTIPS = [
    ('index', "$index"),
    ("x", "$x"),
    ("y", "$y"),
    ("value", "@image")
    ]

    fh_re = figure(title="re of roots of polynom: {}".format(P.poly_text), tools=TOOLS, tooltips=TOOLTIPS,
               match_aspect=True, x_range=[-10,10], y_range=[-10,10])
    fh_re.grid.visible = True
    
    color_mapper = LinearColorMapper(palette="Viridis256", low=np.min(data[:]), high= np.max(data[:]))
    
    fh_re.image(image=[data], color_mapper=color_mapper, x=[-10], y=[-10], dw=[20], dh=[20])
    color_bar = ColorBar(color_mapper=color_mapper, label_standoff=12, ticker=BasicTicker(), border_line_color=None, location=(0,0))
    fh_re.add_layout(color_bar, 'right')
    
    data = np.imag(roots)
    fh_im = figure(title="im of roots of polynom: {}".format(P.poly_text), tools=TOOLS, tooltips=TOOLTIPS,
               match_aspect=True, x_range=[-10,10], y_range=[-10,10])
    fh_im.grid.visible = True
    color_mapper = LinearColorMapper(palette="Viridis256", low=np.min(data[:]), high= np.max(data[:]))
    fh_im.image(image=[data], color_mapper=color_mapper, x=[-10], y=[-10], dw=[20], dh=[20])
    color_bar = ColorBar(color_mapper=color_mapper, label_standoff=12, ticker=BasicTicker(), border_line_color=None, location=(0,0))
    fh_im.add_layout(color_bar, 'right')
    
    output_file("roots.html")
    
    show(row(fh_re, fh_im, sizing_mode="stretch_both"))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-nx", type=int, required=False, default=300, help="number of samples over OX in range (-10, 10)")
    parser.add_argument("-ny", type=int, required=False, default=300, help="number of samples over OY in range (-10, 10)")
    args = parser.parse_args()
    
    P = Poly()
    
    P.set_poly([1,0, 2, 4, -5])
    
    print(P.ev(1))
    print(P.evd(1))
    
    nx = args.nx
    ny = args.ny
    print ("nx = {}".format(nx))
    print ("ny = {}".format(ny))
    
    roots = np.zeros([nx, ny], dtype=np.complex)
    
    for idxre, re in enumerate(np.linspace(-10,10,nx)):
        for idxim, im in enumerate(np.linspace(-10, 10, ny)):
            roots[idxre, idxim] = P.get_root(re + im* 1j, 1e-8)
            
    gen_figure(roots)