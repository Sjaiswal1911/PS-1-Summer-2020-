#tuples are immutable sequence of Python objects

#creating a tuple
tup1 = ('science','commerce','2000','2002')
tup2 = (1,2,3,4,5)
tup3 = "a", "b", "c", "d", "e"
print(tup1 ,"\n", tup2, "\n", tup3)


#creating an empty tuple
tup4 = ()


#creating a tuple with one value, still needs a comma
tup5 = ("one",)


#accessing values
print("tup1[0]:",tup1[0])
print("tup2[1:5]:", tup2[1:5]) #prints tup[i], i = 1 to i =4


#updating tuples
tup6 = (12, 34.56);
tup7 = ('abc', 'xyz');

# Following action is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup8 = tup6 + tup7;
print (tup8);


#deleting tuples

tup = {"python", "XML", "2020", "PS1"}
print(tup)
del tup
print("After deleting tuple:")
print(tup)
#this produces an error as tup doesn't exist anymore

