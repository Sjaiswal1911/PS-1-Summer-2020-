# Built in class Attributes
# __dict__ : Dictionary containing class' namespace
# __doc__ : Class Documentation string or none , if undefined
# __ name__ : Class Name
# __module__ : Module name in which the class is defined
# __bases__ : Tuple contaning base classes inorfer of occurence

class Student:
   'Common base class for all employees'
   stdcount = 0

   def __init__(self, name, stipend):
      self.name = name
      self.stipend = stipend
      Student.stdcount += 1

   def displayCount(self):
     print ("Total Employee %d" % Student.stdcount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Stipend: ", self.stipend)

emp1 = Student("Sarthak", 20000)
emp2 = Student("Shreyas", 5000)
print ("Employee.__doc__:", Student.__doc__)
print ("Employee.__name__:", Student.__name__)
print ("Employee.__module__:", Student.__module__)
print ("Employee.__bases__:", Student.__bases__)
print ("Employee.__dict__:", Student.__dict__ )
