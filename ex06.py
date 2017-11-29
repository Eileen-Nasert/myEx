print "ex06"
print "Strings and Text\n" 

x = "There are %d types of people." % (10) # assigning value to x (which is the phrase) and assigning 10 to %d
binary = "binary" 
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not) # assigning value to y (which is the phrase) and the stuff in the () to the two %s

print x
print y
print "I said: %r." % (x)
print "I also said: '%s'." % (y)
hilarious = True
joke_evaluation = "Isn`t that joke funny?! %r"
print joke_evaluation % hilarious
w = "This is the left side of..."
e = "a string with a right side."
print w + e

# %s is for assigning worlds, %d is for assigning digits/numbers"
# QUESTION: What is %r for?"