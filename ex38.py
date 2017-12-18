print "Do Things to Lists\n"

ten_things = "Appels Oranges Cows Telephone Light Sugar"
print "Wait there are not ten things in that list. Let's fix that."

stuff = ten_things.split(' ') #splits first List at the spaces in between words and names that new list stuff
more_stuff =["Day","Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # loop only runs until stuff-list until Number 10, so list has 11 items 
	next_one = more_stuff.pop() #not sure what this does
	print "Adding; ", next_one
	stuff.append(next_one) # appends next_one variable (which is basically the more_stuff list)
	print "There are %d items now." %len(stuff)

print "There we go:", stuff

print "Let's do some things with stuff."

print stuff[1] #prints 2nd item in stuff -> Orange
print stuff[-1] #prints last position in suff -> Corn
print stuff.pop() #?
print ' '.join(stuff) #?
print '#'.join(stuff[3:5]) #joins with hash 3rd to 4th position and ends at fifth position ->Telephone#Light 	