# Dictionaries
# elements are stored with repsect to keys
# delcared within ''{}'' curly brackets

# Accessing values
dict = {'Name' : 'Sarthak', 'Age' : '19', 'Year' : 'Second'}
print("dict['Name']:", dict['Name'])
print("dict['Age']", dict['Age'])


# Updating Dictionary
dict['Age'] = 20;


#Add new Entry
dict['College'] = "Bits Goa"
dict['PS1'] = "Parinati Solutions"
print("dict['College']:", dict['College'])


# Delete Entry
# Delete single Entry
del dict['PS1']

# Delete all the entries in Dictionary
dict.clear()

# Delete the Dictionary
del dict


# Property of dictionary keys
# When two duplicate keys are entered, the last one is considered.

dict = {'Name' : 'john_Doe', 'Age' : '19', 'College' : 'Bits', 'Name'
: 'Sarthak'}
print("dict['Name']:" ,dict['Name'])

# keys must be immutable hence Strings, Numbers or tuplrs
# List cannot act as key to a dictionary
#   dict = {['Name'] : 'Sarthak', 'Age' : '19'}
#   print("dict['Name']:", dict['Name'])
# the above code produces error
