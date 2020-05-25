# LIST METHODS continued

# Pop
# list_name.pop()
# Removes and returns last object or obj from the list
# default index is '-1' i.e last element
list1 = ['physics', 'Biology', 'chemistry', 'maths']
list1.pop()
print ("list now : ", list1)
# pop by index
# list_name.pop(index))
list1.pop(1)
print ("list now : ", list1)


# Remove
# list.remove(obj)
# removes object obj from list
list2 = ['paras', 'Brijesh', 'Chainika', 'Mahesh']
print("List before removing:", list2)
list2.remove('Chainika')
print ("list now : ", list2)
list2.remove('Mahesh')
print ("list now : ", list2)


# Reverse
# list. reverse()
# Reverses objects of list in place
list3 = ['Sarthak', 'Rishabh', 'Riddhiman', 'Shreayas', 'Advait']
print("List before:", list3)
list3.reverse()
print("List now:" , list3)


# Sort
# list.sort()
# Sorts objects of list, use compare func if given
list4 = ['physics', 'Biology', 'chemistry', 'maths']
print("Before sorting:", list4)
list1.sort()
print ("list now : ", list1)

#
