# The following example teaches us concepts like Inheritance
# It also focuses on type of relationship i.e is-a VS has-a type




#Animal is-a object
class Animal(object):
    pass

#Dog is-a animal i.e Animal is the super class
class Dog(Animal):

            def __init__(self,name):
                #dog has-a name
                self.name = name

# cat is-a Animal
class Cat(Animal):

            def __init__(self,name):
                #cat has-a name
                self.name = name

# person is-a object
class Person(obejct):

            def __init__(self,name):
                #each person has-a name
                self.name = name

                #person has a pet of some kind
                self.pet = None

#each employee is a Person
class Employee(Person):

            def __init__(self , name , salary):
                ##calling the super class constuctor
                super(Employee,self).__init__(name)
                #every emplyee also has-a salary
                self_salary = salary

class Fish(object):
            pass

# every Salmon is-a Fish
class Salmon(Fish):
            pass

# every halibut is-a Fish
class Halibut(Fish):
            pass

## rover is-a Dog
rover = Dog("Rover")

# satan is-a Cat
satan = Cat("Satan")

#mary is-a Person
mary = Person("Mary")

# mary has a pet , who is satan
mary.pet = satan

#frank is-a Employee
frank = Employee("Frank",120000)
#frank has-a pet ,who is rover
frank.pet = rover

#flipper is a Fish
flipper = Fish()

#crouse is a Salmon
crouse = Salmon()

#harry is a Halibut
harry = Halibut()
