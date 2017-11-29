print "ex24"
print "More Practice\n"
 
print "Let's use everything we've learned so far in a script"
print 'You\'d need to know \'bout escapes with \\ that \nnewlines and \t tabs.\n' 

poem = """ 
\tThe lovely world
and it really doesn't matter
what I write here... \nand how long,
because I've used three double-quotes 
\n(three single-quotes is also possible)\n
to begin and end these lines \tof text.
"""

print "-----------"
print poem
print "-----------\n"

result_calc1 = 10 - 2 + 3 * 2
print "This should be fourteen: %s\n" %result_calc1

print "Wizzarding math with BertiBotts Beans from the Harry Potter Books:"
def secret_Harry_Potter_formula(started_variable):
	bertiebotts_beans = started_variable * 500 # inside a function the variable is temporary, when it is returned it can be assigned to a new variable
	jars = bertiebotts_beans / 10
	boxes = jars / 2
	return bertiebotts_beans, jars, boxes # local variables: these are the names of the 3 variables within the function 
	
start_point = 2
beans, jars, boxes = secret_Harry_Potter_formula(start_point) 
# we run the function defined above and use start_point variable
# and because secret_Harry_Potter_formula returns three values, we need three variables 
# to assign them to, in this case beans, jars, and boxes

print "With a starting point of: %d" % (start_point)
print "We'd have %d beans, %d jars, and %d boxes." % (beans, jars, boxes)

start_point = start_point / 2 # modified start_point variable, variation of increment function

print "We can also do that this way:" # next line calls function immediately and leaves out calling local variables)
print "We'd have %d beans, %d jars, and %d boxes." % (secret_Harry_Potter_formula(start_point))
