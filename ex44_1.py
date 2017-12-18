print "ex44 -01 - Inheritance versus Composition\n"
print "passing on behaviour of classes\n"

class Parent(object):

	def implicit(self):
		print "Parent implicit()"
		
class Child(Parent):
	pass # child is undefined class and pass gives it all trates of class Parent
	
dad = Parent() # function parent in assigned to variable dad
son = Child()

dad.implicit()
son.implicit()
