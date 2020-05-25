 Basic list operations

# Length
# len(list_name)
list1 = ['a','b','c']
list2 = ["Sarthak", "Advait", "Shivashankar", "Rishabh"]
print('list1:', list1)
print(len(list1))
print('list2:', list2)
print(len(list2))
#also worls this way
print("[1,2,3] and length is:" , len([1,2,3]))

# concatenation
# list_result = list1 + list2
list3 = ["Riddhiman"]
list4 = list2 + list3
print("List after concatenation is ", list4)
#also be written as
# print(list2 + list3)


# Repetition
# list_result = list * n
list5 = ['Hi!'] * 4
print("After repetition :" , list5)
# can also be written as
# print(['Hi!' * 4])


# Membership
# elem in list
# returns boolean values True or False
print("Sarthak" in list2)
print("Srininvasan" in list4)


# Iteration
# for elem in list[]
for student in list4:
    print(student, end = '\t')
print() Basic list operations

# Length
# len(list_name)
list1 = ['a','b','c']
list2 = ["Sarthak", "Advait", "Shivashankar", "Rishabh"]
print('list1:', list1)
print(len(list1))
print('list2:', list2)
print(len(list2))
#also worls this way
print("[1,2,3] and length is:" , len([1,2,3]))

# concatenation
# list_result = list1 + list2
list3 = ["Riddhiman"]
list4 = list2 + list3
print("List after concatenation is ", list4)
#also be written as
# print(list2 + list3)


# Repetition
# list_result = list * n
list5 = ['Hi!'] * 4
print("After repetition :" , list5)
# can also be written as
# print(['Hi!' * 4])


# Membership
# elem in list
# returns boolean values True or False
print("Sarthak" in list2)
print("Srininvasan" in list4)


# Iteration
# for elem in list[]
for student in list4:
    print(student, end = '\t')
print()
