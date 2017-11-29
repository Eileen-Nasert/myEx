print "ex33"
print "While Loops\n"

# while True:
#	print "this is will run forever" #control + c => stops an endless loop

i = 0 # creating a variable
numbers = [] # creating a variable for an empty list

while i < 6: # while x is less then six this loop will run
	print "At the top i is %d" %i #it will append the current value of x each loop
	numbers.append(i)
	i = i + 1 #increment i is now 1
	print "Numbers now: ", numbers # 
	print "At the bottom i is %d" %i

print "The numbers: " # this sentence will only be printed once

for i in numbers: # this will print all items in the list numbers
	print i, # because of comma the items of list will print in a row
	

# study drill: using one argument in def
print "convert while-loop into function with one argument"
def drill_1(n): #argument called n is the amount of items we will have in myLst_1
	i = 0
	myLst_1 = []
	while i < n:
		print "Item: %d" %i
		myLst_1.append(i)
		i = i + 1
	print myLst_1

# this will call the function def drill_1
print "\nUsing drill_1 with n = 8"
drill_1(8)

# study drill: using two arguments in def
print "convert while-loop into function with two arguments"
def drill_2(n, s): #argument called s is increment steps
	i = 0
	myLst_2 = []
	while i < n:
		print "Item: %d" %i
		myLst_2.append(i)
		i = i + s
	print myLst_2
	
#this will call function def drill_2
print "\nUsing drill_1 with n = 6 and s = 2"
drill_2(6, 2)

#study drill: using a for-loop in def and range
print "for-loop instead of while-loop in def"
def drill_3(n, s):
	myLst_3 = range(0,n,s)
	for i in myLst_3:
		print "Item: %d" %i
	print myLst_3

drill_3(16,3)



