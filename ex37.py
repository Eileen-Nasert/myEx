print "ex35"
print "Branches and Functions\nFind the Gold Room"

from sys import exit

#defining function for gold room
def gold_room():
	print "This room is full of gold. How much do you take? Enter a number."
	
	choice = raw_input("> ")
	if "0" in choice or "1" in choice:
		how_much = int(choice) #turns string "1" and "2" into an integer(number)
	else:
		dead("Man, learn how to type a number.") #dead is defined below
		
	if how_much <50: # i
		print "Nice,you're not too greedy, you win!"
		exit(0) #exit is an imported system function
	else:
		dead("You greedy bastard! You're dead.")
	
		
	
	print "The bear has a bunch of honey."
	print "The fat bear is in front of another door."
	print "How are you going to move the bear?"
	bear_moved = False # creating boolean function
	
	while True:
		choice = raw_input("> ")
		
		if choice == "take honey":
			dead("The bear looks at you then slaps your face off.")
		elif choice == "taunt bear" and not bear_moved:
			print "The bear has moved from the door. You can go though it now."
			bear_moved = True
		elif choice == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chews your leg off.")
		elif choice == "open door" and bear_moved:
			gold_room() #now function gold_room is run
		else:
			print "I got no idea what that means."
		




elif door == "2":
	print "You stare into the endless abyss at Cthulhu's retina"
	print "1. Blueberries."
	print "2. Yellow jacket clothespins."
	print "3. Understanding revovers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"

else:
	print "You stumble around and fall on a knife and die. Good job!"
	

def dead(why): #why refers to e.g. Well that was tasty, ...
	print why, "Good job!" # runs reason and ads good job!
	exit(0)


