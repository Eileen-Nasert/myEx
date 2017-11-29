# before running the program in terminal you must assign names to variables
# type in command line: 
# $ python ex13.py orange grapefruit pineapple 
# ex13.py is assigned to script, orange is assigned to variable first, usw.

print "ex13"
print "Parameters, Unpacking, Variables\n"

from sys import argv # imports module from Python module set
script, first, second, third = argv # assignes the module to four different variables

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# modules = libraries
# difference between argv (input on command line) and raw_input (input on terminal)