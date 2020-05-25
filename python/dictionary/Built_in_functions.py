# BUILT-IN functions

# Compare:
# cmp(dict1, dict2)
# returns -1 -> dict1 < dict2
# returns 0 -> dict1 == dict2
# returns 1 -> dict1 > dict2
dict1 = {'Name': 'Sarthak', 'Age': 19};
dict2 = {'Name': 'Shreyas', 'Age': 18};
dict3 = {'Name': 'Hari', 'Age': 20};
dict4 = {'Name': 'Devshree', 'Age': 18};
print ("Return Value : %d" %  cmp (dict1, dict2))
print ("Return Value : %d" %  cmp (dict2, dict3))
print ("Return Value : %d" %  cmp (dict1, dict4))


# length
# len(dict_name)
# return the no. of elements inside the Dictionary
dict =  {'Name': 'Mani', 'Age': 24, 'Company': 'IBM'}
print ("Length : %d" % len (dict))


# toString
# str(dict_name)
# produces a printable string representation of the Dictionary
dict1 = {'Name': 'Raj', 'Age': 38, 'Proffession': 'Doctor'}
print ("Equivalent String : %s" % str (dict1))


# type
# type(variable)
dict2 = {'Name': 'Saumya', 'Age': 22, 'Branch': 'EEE'}
print ("Variable Type : %s" %  type (dict2))
