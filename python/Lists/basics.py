# LISTS
# most versatile data type in Python

# Creating lists
# lsit_name = [elem_1, .. , elem_n]
list1 = ['physics', 'chemistry', 2002, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];

# Accessing values
# list_name[index]
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])


# Updating lists
# list_name = index = value
list = ['Sarthak', 'Jaiswal', 2000, 'CS']
print("Value available at index 2 : ", list[2])
list[2] = 2001
print ("New value available at index 2 : ", list[2])


# deleting list elements
# del list_name[index]
del list[2]
print ("After deleting value at index 2 : ", list)
