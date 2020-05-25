# basic operations

# length
tup1 = ("Sarthak", "Jaiswal", "BITS-Goa", "2020")
print(len(tup1))


# concatenation
tup2 = ("Parinati", "Solutions", "Goa")
tup_result = tup1 + tup2
print(tup_result)
# can also be done as
#print(tup1 + tup2)


# repetition
tup3 = ("Hi!",)
tup4 = tup3 * 4
# also written as
# tup4 = ("Hi!",) * 4
print(tup4)


# membership
tup5 = ("Goa", "Mumbai", "Bangalore", "India")
print("Goa" in tup5)
#returns boolean value True or False


#iteration
tup6 = (1,2,3,4,5,6,7)
for i in tup6:
    print(i)
#prints the elements in tuple


#garbage colection

del(tup1)
del(tup3)
# amd so on...
