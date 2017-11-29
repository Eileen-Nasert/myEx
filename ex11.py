print "ex11"
print "Asking Questions\n"

print "How old are you?",
age = raw_input()
print "How tall are you?" #without comma at the end your answer will appear on new line
height = raw_input() 
print "Remember: just 'input ()' will try to convert what \n was typed, 'raw_input ()' will not convert"
print "How much do you weigh?",
weight = raw_input()
print "So, you're %r old, %r tall and %r heavy." % (age, height, weight)