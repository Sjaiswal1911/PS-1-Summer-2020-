# Privacy and control

# Data hiding
# declare the attribute with double underscore '__' as prefix
class JustCounter:
   __secretCount = 0

   def count(self):
      self.__secretCount += 1
      print (self.__secretCount)

   def print_count(self):
       print(self.__secretCount)

counter = JustCounter()
counter.count()
counter.count()
counter.print_count()
print (counter.__secretCount)
# this produces an error
