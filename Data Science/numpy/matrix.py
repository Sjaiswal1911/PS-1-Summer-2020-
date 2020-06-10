import numpy as np

# ones
# numpy.ones([row,columns], type)
mat = np.ones([2,3], int)
print(mat.shape)
print(mat)


# Transpose
# n.T
mat = mat.T
print(mat.shape)
print(mat)


# Data type
# returns the type of data in the array
print(mat.dtype)


# asType
# n = n.astpye(type)
# change the datatype to specified type
mat = mat.astype('f')
print(mat.dtype)
