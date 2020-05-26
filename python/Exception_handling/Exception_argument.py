# Exception as an argument
# try:
#    You do your operations here
#    ......................
# except ExceptionType as Argument:
#    You can print value of Argument here...

def temp_convert(var):
   try:
      return int(var)
   except ValueError as Argument:
      print ("The argument does not contain numbers\n", Argument)

# Call above function here.
temp_convert("xyz")
