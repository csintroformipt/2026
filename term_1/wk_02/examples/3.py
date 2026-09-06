import numpy as np

ar = np.zeros([10,10], dtype='int')
print(ar)
print(ar.shape)
print(ar.size)
print(type(ar))
print(ar[0])
print(ar[0:5])
print(ar[0:5][:-1])
print(ar[0:5][1:5:2])
print(ar[:])
print(id(ar))
#%%
ar = np.ones([10,10], dtype='int')
print(ar)
print(ar.shape)
print(ar.size)
print(type(ar))
print(ar[0])
print(ar[0:5])
print(ar[0:5][:-1])
print(ar[0:5][1:5:2])
print(ar[:])
print(id(ar))
#%%
sizes = [10, 10]
ar = np.arange(np.prod(sizes)).reshape(sizes)
print(ar)
print(ar.shape)
print(ar.size)
print(type(ar))
print(ar[0])
print(ar[0:5])
print(ar[0:5][:-1])
print(ar[0:5][1:5:2])
print(ar[:])
print(id(ar))
#%%
b = ar
print(b)
print(ar)
b[0,0] = 100
print(b)
print(ar)
print(id(b), id(ar))

b = ar.copy()
print(id(b), id(ar))
b = ar[:]
print(id(b), id(ar))
#%%

print(np.unique(ar[:], return_counts=True))

#%%
b = 2*np.eye(10, dtype=np.float)
print(b)
diag_values = np.diag(b, 1)
print(np.diag(np.ones([9],dtype=np.float), 1))
b -= np.diag(np.ones([9],dtype=np.float), 1)
b -= np.diag(np.ones([9],dtype=np.float), -1)
print(b)

#%%
rhs = np.zeros(b.shape[0])
print(b.dtype)
rhs[0] = 100
rhs[-1] = 1
print(rhs)
print(np.linalg.solve(b, rhs))
 
#%%
ar[:] = 1
#%%
res = np.linalg.solve(b, rhs)
#%%
from matplotlib import pyplot as plt
plt.figure()
plt.plot(res)
plt.show()