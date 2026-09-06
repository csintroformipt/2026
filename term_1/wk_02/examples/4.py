#!/bin/python3
# please refer to the documentation:
#   https://numpy.org/doc/stable/reference/generated/numpy.fromfile.html
#   https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html
#   https://numpy.org/doc/stable/reference/generated/numpy.ndarray.tofile.html#numpy.ndarray.tofile
#   https://numpy.org/doc/stable/reference/generated/numpy.load.html#numpy.load
#   https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html  

import numpy as np

my_data = np.loadtxt("my_junk_file.txt")

print(my_data)

#%%

#let's put some junk data to my data variable
my_data_from_bin = dict(a=1, b='sometext')
with open('my_junk_file.bin', 'rb') as file:
    my_data_from_bin = np.fromfile(file, dtype=np.int32, count=-1)
    
print (my_data_from_bin)

#%%
np.save('numpy_junk_file.npy', my_data_from_bin)
new_array = np.load('numpy_junk_file.npy')
print('saved&loaded by numpy data:', new_array)