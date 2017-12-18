print "ex44 - Inheritance versus Composition\n"


# passing on behaviour of classes
class Parent(object):

	def implicit(self):
		print "Parent implicit()"
		
class Child(Parent):
	pass # child is undefined class and pass gives it all trates of class Parent
	
dad = Parent() # function parent in assigned to variable dad
son = Child()

dad.implicit()
son.implicit()

# Override Explicitly

class Parent(object):

	def override(self):
		print "Parent override()"

class Child(Parent):

	def override(self):
		print "Child override()"
	
dad = Parent() 
son = Child()

dad.override()
son.override() # son is an instance of child and child overrides that function by defining it's own version

# Alter before of After
class Parent(object):

	 def altered(self):
	 	print "Parent altered()"
	 
class Child (Parent):

	def altered(self):
		print "Child, before Parent altered()"
		super(child, self).altered() #super is built in function aware of inheritance and calls on parent class
		print "Chuld, after Parent altered()"
	
dad = Parent() 
son = Child()

dad.altered()
son.altered()

