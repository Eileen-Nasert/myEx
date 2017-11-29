print "ex19"
print "Function and Variables\n"

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % (cheese_count)
	print "You have %d boxes of crackers!" % (boxes_of_crackers)
	print "That's enough for a party. \n"
	
	
# Now we fill in the previous function:

# first way: putting in numbers	
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# second way: creating variables and calling them in the functions
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# third way: doing math in the function
print "We can even do math inside too:"
cheese_and_crackers(10 +20, 5 + 6)

# fourth way: doing math with variables and numbers
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)