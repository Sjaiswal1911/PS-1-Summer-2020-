# Scope of Variables
# This depends on where you have declared a variable.

# global Variables : can be accessed anywhere
# local Variables  : accessible only inside the function they are defined in

total = 0   # This is global variable.
# Function definition is here
def sum( arg1, arg2 ):
   # Add both the parameters and return them."
   total = arg1 + arg2; # Here total is local variable.
   print ("Inside the function local total : ", total)
   return total

# Now you can call sum function
sum( 10, 20 )
print ("Outside the function global total : ", total )
