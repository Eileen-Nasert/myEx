# $ ex16.py ex16_test.txt

print "ex 16"
print "Reading and Writing Files\n"

# commands/functions used to modify files:
# close() -> closes file
# read() -> reads content of file
# readline() -> reads one line of text file
# truncate() -> empties file
# write('stuff') -> writes "stuff" to the file (this is a command that needs a parameter)

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN," # if filen doesn't exists it will be created

raw_input("?")

print "Opening the file..."
target = open(filename, 'w') 
# w stands for write, r for read, a for append -> which means adding on to text
# r+ allows you to read and write
# w+ allows you to write and read

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input ("line 1: ") 
line2 = raw_input ("line 2: ")
line3 = raw_input ("line 3: ")

print "I'm goint to write these to the file."

target.write(line1) # take whatever is in line 1 and write it into the object: target textfile
target.write("\n") # linebreak
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it."
target.close()

# type pydoc file in terminal to get lots of information in commands
