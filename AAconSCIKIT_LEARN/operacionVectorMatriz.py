import numpy as np
from numpy import linalg

v = np.array([1,2,3])
print(v)
print(v[1])

m = np.array([[1,2,3],[0,1,4],[5,6,0]])
print(m)

print(m[0,0])
print(m[2,1])

#------------algunas operaciones de algebra lineal--------------------------
print(v @ m) # multiplicacion de vector y matriz
m_inv = linalg.inv(m) # inversa de la maris m
print(m_inv)

print(m @ m_inv) # multiplicacin matriz por su inversa