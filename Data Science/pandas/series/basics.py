import pandas as pd

# creating a new Series
animals = ['Tiger', 'Bear', 'Moose']
pd.Series(animals)

numbers = {'One': 1,'Two' : 2,'Three' : 3]
pd.Series(numbers)


# Accessing data
# iloc
# returns the data at the specified index number
print(animals.iloc[1])

# loc
# returns the data at the specified index location
print(numbers.loc['One'])


# Explicit index type
s = pd.Series(['Tiger', 'Bear', 'Moose'], index=['India', 'America', 'Canada'])
s
