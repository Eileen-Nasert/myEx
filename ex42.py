print "ex42\n"

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass

## Dog is-a object
class Dog(Animal):

	def __init__(self, name):
	## self has-a name (and is set to name)
	self.name = name

## Cat is-a Animal
class Cat(Animal):

	def __init__(self, name):
	## self has-a name (and is set to name)
	self.name = name

## Person is a object
class Person(object):

	def __init__(self, name):
		# self has-a name and is set to name)
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## Employee is-a Person
class Employee(Person):

	def __init__(self, name, salary):
	## ?? super (with function Employee and self) has-a initiation (with funncion name)=
	super(Employee, self).__init__(name)
	## self has-a salary
	self.salary = salary

## fish is-a object
class Fish(object):
	pass

## Salmon is-a fish
class Salmon(Fish):
	pass

## halibut is a fish
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog(”Rover”)

## satan is-a cat
satan = Cat(”Satan”)

## mary is-a Person (with function Mary)
mary = Person(”Mary”)

## Mary has-a pet  that is-a satan
mary.pet = satan

## frank is a employee with function frank and 120000
frank = Employee(”Frank”, 120000)

## frank has-a pet, that is-a rover
frank.pet = rover

## ?? flipper is a fish, crouse is a Salmon
flipper = Fish()

crouse = Salmon()

## Harry is a Halibut
harry = Halibut()