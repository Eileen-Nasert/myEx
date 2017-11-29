print "ex18"
print "Names, Variables, Code, Functions\n"

# this one is like your scripts with argv
def print_two(*args): # def means we will create a function naming it 'print_two' with a list of arguments defined below
	arg1, arg2 = args # unpacking args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# *args is actually pointless, we can just do this
def print_two_again(arg1, arg2): # simply put names of two new arguments in ()
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % (arg1)
	
# this one takes no arguments
def print_none():
	print "I got nothing."
	
print_two ("Eileen", "Nasert") # print what is in line 7
print_two_again ("Eileen", "Nasert")  #print what is in line 11
print_one ("First!") # print what is in line 15
print_none() # print what is in line 19, but it does not need an argument