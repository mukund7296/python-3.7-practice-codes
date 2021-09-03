#creating the matrix

import numpy as np

A=np.array([[1,2,4],[2,4,3],[0,1,1]])
print(A)
print(A[1])
print(A[1][1])

print(A.sum())

#generate the matrix
B=np.arange(1,10)
B.reshape(3,3)
print(B)

