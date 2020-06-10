# Creating arrays
import numpy as np

# Creatiing an Array
# from a list
mylist = [1,2,3]
n = np.array(mylist)
print(n)

# wo dimensional array
mylist2 = ['a','b','c']
n2 = np.array([mylist,mylist2])
print(n2.shape)  # prints the dimension of Matrix
print(n2)

# Arange
# numpy.arange(start,end,step)
# creates an array [start,end) with differnce of 'step'
n3 = np.arange(0,30,2)
print(n3.shape)
print(n3)


# reshape
# n.reshape(row,column)
n3 = n3.reshape(3,5)
print(n3)
