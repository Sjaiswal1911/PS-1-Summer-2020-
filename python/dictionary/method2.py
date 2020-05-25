# Dictionary methods

# Items
# dict.items()
# Returns a list of dict's (key, value) tuple pairs
dict = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" %  dict.items())


# keys
# dict.keys()
# Returns a list of dictionaries' keys
dict2 = {'Name': 'Sarthak', 'Age': 20, 'Branch' : 'Goa'}
print ("Value : %s" %  dict2.keys())


# setDefualt
# dict.setdefault(key, default = None)
# Similar to get(), but will set dict[key] = default
#if key is not already in dict
dict3 = {'City': 'Mumbai', 'State': 'Maharashtra'}
print ("Value : %s" %  dict3.setdefault('State', None))
print ("Value : %s" %  dict3.setdefault('Country', None))
print (dict3)


# Update
# dict.update(dict2)
# Adds dictionary dict2's key-values pairs to dict
dict4 = {'Name' : 'Lewis Hamilton', 'Team' : 'Mercedes-Petronas',
'Championships' : 6}
dict5 = {'Team pricnipal' : 'Toto wolff' , 'Engineer' : 'Bono'}
dict4.update(dict5)
print("Update dict is :" , dict4)


# values
# dict.values()
# returns lsit of dictionaries' dict values
dict6 = {'Sex': 'female', 'Age': 18, 'Name': 'Varsha'}
print ("Values : ",  list(dict6.values()))


# iterartion
# for key, elem in list(dict_name.items()):


