# Garbage Collection

# Destructor
# __del__()
# destructs or de-alocates the memory when class isn't gonnabe used.
class Point:
   def __init__( self, x=0, y=0):
      self.x = x
      self.y = y
   def __del__(self):
      class_name = self.__class__.__name__
      print (class_name, "destroyed")

pt1 = Point()
pt2 = pt1
pt3 = pt1
print (id(pt1), id(pt2), id(pt3))   # prints the ids of the obejcts
del pt1
del pt2
del pt3


# After the three instances of the Point class has been destoryed:
# the destructor gets initalized and fress the memory
# Also message : Point destroyed is displayed.
