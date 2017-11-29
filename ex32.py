print "ex32"
print "Loops and Lists\n"

#creating three lists/arrays (with square brakets and commas)
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters'] # using different data types

# this first kind of for-loop goes through a list (for aka for-loop) 
for number in the_count: # number is a new variable; 'in' specifies the list we're pulling from
	print "This is count %d" % number # using %d because number/digits
	
# same as above
for fruit in fruits:
	print "A fruit of type: %s" % fruit # using %s because strings/words

# we can go through mixed lists as well
# notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i # r is representation/raw data because we don't know what type of input
	
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 count
for i in range(0, 6):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i) # add i onto elements, the previously empty list
	
fot i in range(0,10,2): #startpoint, endpoint
	print i,
	
# now we can print out list with appended numbers
for i in elements:
	print "Element was. %d" % i
	
elements2 = range(6) # this step combines three steps beforehand
for i in elements2:
	print "elements2 item was %d" % i
	
# while lopp not defined amount, it repeats as long as condition is met
# for loop has a precice range
	