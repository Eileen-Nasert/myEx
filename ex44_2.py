print "ex44 -02 - Inheritance versus Composition\n"
print "Override Explicitly\n"

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
