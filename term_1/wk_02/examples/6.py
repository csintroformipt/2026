# please refer to the documentation 
#   https://numpy.org/devdocs/reference/routines.linalg.html


import numpy as np
#%%
a = np.linspace(1, 100, 100)

print(np.dot(a,a))

#%%

a = np.arange(3*4*5*6).reshape((3,4,5,6))

b = np.arange(3*4*5*6)[::-1].reshape((5,4,6,3))

print(np.dot(a, b)[2,3,2,1,2,2]

#%%
w, v = np.linalg.eig(np.diag((1, 2, 3)))

print(w, v)