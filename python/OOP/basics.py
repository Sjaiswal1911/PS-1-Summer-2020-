# Classes and objects

# Creating Classes
# class ClassName:
#   'Optional class documentation string'
#   class_suite
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


# Creating instances
# This would create first object of Employee class
emp1 = Employee("Zaina", 2000)
# This would create second object of Employee class
emp2 = Employee("Mahesh", 5000)


# Accessing Attributes
emp1.displayEmployee()
emp2.displayEmployee()
print ("Total Employee %d" % Employee.empCount)


# Add, remove, modify attributes
emp1.salary = 7000  # Add an 'salary' attribute.
emp1.name = 'xyz'  # Modify 'age' attribute.
del emp1.salary  # Delete 'age' attribute.

#
