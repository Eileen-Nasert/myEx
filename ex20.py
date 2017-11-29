# $ python ex20.py ex20_test.txt

print "ex20"
print "Functions and Files\n"

from sys import argv

script, input_file = argv

# This function will display the entire text
def print_all(f): # f stands for input_file , put I could name it anyway I want
	print f.read() # read will display the entire text of f
	
# This function will go to the beginning of the file
def rewind(f): # naming this function rewind
	f.seek(0) # seek is new command meaning go particular place in f (in this case 0 = beginning)
	
# This function will print file one line at a time
def print_a_line(line_count, f):
	print line_count, f.readline()


# Now we fill in the previous function:	
current_file = open(input_file) # open input_file and assign it to variable current_file

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

current_line = 1 # defining the variable as 1 (line 1)
print_a_line(current_line, current_file)

current_line = current_line + 1 # this is a incrementing function, new current line is line 2
print_a_line(current_line, current_file)

current_line = current_line + 1 # this is a incrementing function, new current line is line 3
print_a_line(current_line, current_file)