print "ex30"
print "Else and If\n - branching commands"

# creating 3 variables:
people = 30
cars = 40
busses = 15

# elif is short for else if 
if cars > people: # first condition
	print "We should take the cars. This if statement will print and skip elif and else."
elif cars < people: # if first condition is not met this is an additional condition 
	print "We should not take the cars."
else: # when if and elif are not met this covers everything else
	print "We can't decide."
	
if busses > cars: # not true therefore skips to elif
	print "That's too many busses."
elif busses < cars: # true 
	print "Maybe we could take the busses. This elif is true and will print"
else:
	print "We still can't decide!"
	
if people > busses: # is ture
	print "Alright, let's just take the busses. Yay this if statement is true."
else:
	print "Fine, let's stay home then."