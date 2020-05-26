# Types of Arguments:

# Required Arguments
# arguments passed must be in correct positional order.
# Number of arguments must match the function definiton while Calling.
def printme( str ):
   "This prints a passed string into this function"
   print (str)
   return

# Now you can call printme function
# printme() -> this produces an error
printme("Hello! my name is Sarthak.")


# Keyword arguments
# Keyword arguments are related to the function calls
# the order of the arguments doesn't matter.
# Function definition is here
def printinfo( name, age ):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinfo( age = 19, name = "Sarthak" )


# Default Arguments
# Assumes a default value if not provided a value in function call
# the argument with default value must be specified at the RHS in funtion definition
def printinf( name, age = 20):
   "This prints a passed info into this function"
   print ("Name: ", name)
   print ("Age ", age)
   return

# Now you can call printinfo function
printinf( age = 20, name = "Sarthak" )
printinf( name = "Sarthak" )


# Variable length Arguments
# the prefix '*' in front of the argument with var-length
def print_var_info( arg1, *vartuple ):
   "This prints a variable passed arguments"
   print ("Output is: ")
   print (arg1)

   for var in vartuple:
      print (var)
   return

# Now you can call printinfo function
print_var_info( 10 )
print_var_info( 70, 60, 50 )
