# $ ex15.py ex15_sample.txt

print "ex15"
print "Reading Files\n"

from sys import argv

script, filename = argv

txt = open(filename) # open is a command that read our text file

print "Here's your file %r;" %(filename)
print txt.read() 
# the dot is an operator, which means: do the operation (read) afer the dot on the object (txt) before the dot
# functions/operations have to have arguments, but in this case there are none, hence the parentheses are empty

# do the whole thing again from within the script -> meaning prompting me from within the script to the file
print "Type the filename again:"
file_again = raw_input(">") 
# the filename we type (e.g. ex15_sample.txt) is taken as raw_input and assigned to variable 'file_again'

txt_again = open(file_again)
# this opens the filename we typed in, opens it and assigns it to variable 'text_again'

print txt_again.read()

# closing objects/variables txt and txt_again by typing a dot and the operation close
txt.close
txt_again.close