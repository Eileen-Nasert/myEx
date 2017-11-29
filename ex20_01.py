# $ python ex20.py ex20_test.txt

from sys import argv

script, input_file = argv

# This function will display the entire text of ex20_test.txt
def print_all(f): # f stands for input_file , put I could name it anyway I want
	print f.read() # read will display the entire text of f
	
# Now we fill in the previous function:
current_file = open(input_file) # open input_file and assign it to variable current_file

print "First let's print the whole file:\n"
print_all(current_file)