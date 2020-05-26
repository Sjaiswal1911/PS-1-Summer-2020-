# Exceptios:
# occurs during executiion of program, dirupts normal flow


# Handling
# try:
#    You do your operations here
#    ......................
# except ExceptionI:
#    If there is ExceptionI, then execute this block.
# except ExceptionII:
#    If there is ExceptionII, then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block.
try:
   fh = open("testfile", "w")
   fh.write("This is my test file for exception handling!!")
except IOError:
   print ("Error: can\'t find file or read data")
else:
   print ("Written content in the file successfully")
   fh.close()
