# BUILT-IN functions for tuples

# Compare
# cmp(tup1, tup2)
# returns integer value
# -1 : tup1 < tup2
# 0 : tup1 == tup2
# 1 : tup1 > tup2
tup1 = ("Sarthak", "Jaiswal")
tup2 = ("Parinati", "Solutions", "Goa")
tup3 = ("Parinati", "Solutions")

print("tup1:", tup1)
print("tup2:", tup2)
print("tup3:", tup3)
#Comparing
print("Comparing tup1 with tup2:" ,cmp(tup1, tup2))
print("Comparing tup2 with tup3", cmp(tup2, tup3))
print("Comparing tup1 with tup3", cmp(tup1, tup3))


# Length
# len(tup_name)
tup = (1,2,3,4,5,6)
print(len(tup))


# Maximum
# max(tuple_name)
# returns the maximum value
tup4 = (128, 159, 200, 560, 6969)
tup5 = ("Sarthak", "Rajesh", "Sart", "Zero")
print("tup4:", tup4)
print("tup5:", tup5)
print("Max of tup4:", max(tup4))
print("Max of tup5:", max(tup5))


# Minimum
# min(tuple_name)
# returns the Minimum value

print("Min of tup4:", min(tup4))
print("Min of tup5:", min(tup5))


# List to tuple
# tuple(seq)
# converts the list 'seq' to a tuple.
# returns a tuple

aList = [123, 'xyz', 'zara', 'abc']
aTuple = tuple(aList)
print ("Tuple elements : ", aTuple)
print(type(aTuple))     # types class 'tuple' 
