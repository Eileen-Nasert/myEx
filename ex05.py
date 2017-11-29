print "ex05"
print "More Variables and Printing\n"

# double-quotes create strings
my_name = 'Eileen'
my_age = 21 # not a lie
my_height = 162 #cm
my_weight = 55 #kg
my_eyes = 'grey blue'
my_teeth = 'white - going on coffee stain'
my_hair = 'light blonde'

print "Let's talk about %s." % my_name
print "I am %d cm tall." % my_height
print "You don't ask a women's weight %d" % my_weight
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# The next line is tricky. Try to get it exactly right.
print "If I add %d, %d and %d I get %d." % (
	my_age, my_weight, my_height, my_age + my_weight + my_height)
	
# %s,r,d are formatters: They take the variable on the right and replace % with the value