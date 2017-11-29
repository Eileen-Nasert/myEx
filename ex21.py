print "ex21"
print "Functions Can Return Something\n"

#defining 4 functions:

def add(a, b): #define function named add and add two arguments named variables a and b
	print "Adding %d + %d" % (a, b) # not necessary, makes script busy
	return a + b # return is special function, which makes a value created by def function available

def subtract(a, b):
	print "SUBSTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b
	
def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	
print "Let's do some math with just functions!"

# Now we fill in the previous function and let them run
# it will end up taling return value of function and assign it to the variable
# creating 4 variables:

age = add(20, 1)
height = subtract(182, 20)
weight = multiply(5, 11)
iq = divide (100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here's a puzzle:"
what = add(age, subtract(height, multiply(weight, divide(iq, 2)))) # work from the inner parentheses out, note order of operation!
# new variable called 'what'

print "That becomes: ", what, "Can you do it by hand?"	
print "QUESTION: Why is each step of puzzle printed and not just the result?"