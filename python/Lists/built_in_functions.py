# BUILT- IN functions

# Max
# max(list)
# Returns item from the list with max value.
list1, list2 = ['C++','Java', 'Python'], [456, 700, 200]
print ("Max value element : ", max(list1))
print ("Max value element : ", max(list2))


# Min
# min(list)
#Returns item from the list with min value.
list1, list2 = ['Ruby','Swift', 'CSS'], [690, 420, 100]
print ("min value element : ", min(list1))
print ("min value element : ", min(list2))


# toList
# list(seq)
# converts tuple to a list
aTuple = (123, 'C++', 'Java', 'Python')
list1 = list(aTuple)
print ("List elements : ", list1)
print("Type of list is.." , type(list1))

#another example
str = "Hello World"
list2 = list(str)
print ("List elements : ", list2)
