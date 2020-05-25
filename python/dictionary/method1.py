# Dictionary methods

# Clear
# dict.clear()
# Removes all elements of dictionary dict
dict = {'Name': 'Sarthak', 'Age': 19, 'College' : "Bits-GOA",
 'Branch' : 'CS' }
print ("Start Len : %d" %  len(dict))
#prints 4
dict.clear()
print ("End Len : %d" %  len(dict))
#prints 0


# Copy
# dict.copy()
# Returns a shallow copy of the dictionary 'dict'
dict1 = {'Name': 'Tvisha', 'Age': 9, 'Class': 'Fourth'}
dict2 = dict1.copy()
print ("New Dictionary : ",dict2)
# shallow copy means a fresh new copy whithout using common reference
# that is changes made to dict2 won't affect dict1 and vice versa


# fromKeys
# dict.fromkeys()
# Create a new dictionary with keys from seq and values set to value.
seq = ('name', 'age', 'sex')
dict = dict.fromkeys(seq)
#cretes a dict whose keys are elements of Tuple 'seq'
print ("New Dictionary : %s" %  str(dict))

# to allot the same element to all keys
dict = dict.fromkeys(seq, 7)
print ("New Dictionary : %s" %  str(dict))
