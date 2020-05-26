# functions
# is a block of organised, reusable code to perform a single , related action

# syntax
# def functionname( parameters ):
#    "function_docstring"
#    function_suite
#    return [expression]


# Defining a function
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return


# Calling a function
printme("This is first call to the user defined function!")
printme("Again second call to the same function")


# Pass by Reference
# default way in python
# change in parameter passed , reflects back in the calling function
def changeme( mylist ):
   "This changes a passed list into this function"
   print ("Values inside the function before change: ", mylist)

   mylist[2]=50
   print ("Values inside the function after change: ", mylist)
   return

# Now you can call changeme function
mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)
