print "ex44 -4 - Inheritance versus Composition\n"
print "All three combined"
print "This is a child is-a parent relationship\n"

class Parent(object):
	
	def override(self):
		print "Parent override()"
	
	def implicit(self):
		print "Parent implicit()"
	
	def altered(self):
		print "Parent altered()"
	
class Child(Parent):
	
	def override(self):
		print "Child override()"
		
	def altered(self):
		print "Child before parent altered()"
		super(Child, self).altered()
		print "Child, after Parent altered()"
		
dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()