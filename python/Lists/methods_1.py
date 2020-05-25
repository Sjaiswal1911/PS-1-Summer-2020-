# LIST METHODS

# Append
# list.append(obj)
# Appends object obj to list
list1 = ['C++', 'Java', 'Python']
print("List before appending is..", list1)
list1.append('Swift')
print ("updated list : ", list1)
del list1


# Count
# list.count(obj)
# Returns count of how many times obj occurs in list
aList = [123, 'xyz', 'zara', 'abc', 123];
print ("Count for 123 : ", aList.count(123))
print ("Count for zara : ", aList.count('zara'))


# Extend
# list.extend(seq)
# Appends the contents of seq to list
list1 = ['physics', 'chemistry', 'maths']
list2 = list(range(5))     #creates list of numbers between 0-4
list1.extend(list2)
print ('Extended List :', list1)


# Index
# list.index(obj)
# Returns the lowest index of obj in the list
print ('Index of chemistry', list1.index('chemistry'))
#print ('Index of C#', list1.index('C#'))
# this produces an error


# Insert
# list.insert(index, obj)
# inserts the obj at 'index' location in list
print("Before insertion:" ,list1)
list1.insert(1, 'Biology')
print ('Final list : ', list1)
