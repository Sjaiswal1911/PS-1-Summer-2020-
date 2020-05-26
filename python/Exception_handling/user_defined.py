# User defined Exceptions
# in python user can define Exceptions
class Networkerror(RuntimeError):
   def __init__(self, arg):
      self.args = arg
# once the above class is defined the follwoing code can raise exp
try:
   raise Networkerror("Bad hostname")
except Networkerror,e:
   print e.args
