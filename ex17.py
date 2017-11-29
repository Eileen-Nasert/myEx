# $ python ex17.py ex17_from.txt ex17_to.txt (these are arbitrary file names)

print "ex17"
print "More files - reading one file and copying it's content to antoher file\n"

from sys import argv # let's us specify information in the command line
from os.path import exists # importing command 'exists' from 'os.path'-library
# exists will return true of file exists (more precisely if file-path is valid)

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

in_file = open(from_file)
indata = in_file.read()

# doing previous two lines in one: indata = open(from_file).read()

print "The input file is %d bytes long" % len(indata) # len = length of file in bytes

print "Does the output file exist? %r " % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abord."
raw_input()

out_file = open (to_file, 'w')
out_file.write(indata) # QUESTION: I don't quite understand these two lines!

print "Alright, all done."
out_file.close()
in_file.close()
# remove in_file.close() and instead do indata.close() if you have used indata as a variable