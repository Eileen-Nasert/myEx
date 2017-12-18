print "ex44 -03 - Inheritance versus Composition\n"

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

