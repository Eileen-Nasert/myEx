print "ex29"
print "What if\n"
print "if statements aka conditionals"

# three numeric variables:
people = 20
cats = 30
dogs = 15

#creating 4 if statements:
if people < cats: # if 20 < 30 => True, meaning the print will run
	print "Too many cats! The world is doomed!"
	
if people > cats: # get's skipped beacause not it's not true
	print "Not many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	
# trying out other Boolean expressions:
if people != dogs:
	print "Yay it worked"

if people > cats and cats > dogs: # False and True => False
	print "This will not print."

if people > cats or cats > dogs: # False or True => True
	print "This will print."
	
# increment 
dogs += 5
# dogs = dogs + 5 = 20 

if people >= dogs: # 20 >= 20 => True, will get printed
	print "People are greater than or equal to dogs." 
	
if people<= dogs: # 20 <= 20 => True, will get printed
	print "People are less than or equal to dogs."
	
if people == dogs: # 20 == 20 => True, will get printed
	print "People are dogs."
