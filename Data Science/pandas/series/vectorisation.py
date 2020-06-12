import numpy as np
import pandas as pd
import timeit

#creating a series
s = pd.Series([100.00, 120.00, 101.00, 3.00])
print(s)

# getting the sum by iteration
total = 0
for item in s:
    total+=item
print(total)

# getting sum by numpy
total = np.sum(s)
print(total)

# Time analysis
t = pd.Series(np.random.randint(0,1000,10000))
print(t.head()) # prints the first 5 elements

# traditional way
%%timeit -n 100
summary = 0
for item in t:
    summary+=item

# vector way by numpy
%%timeit -n 100
summary = np.sum(s)
