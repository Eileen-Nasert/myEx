# name question
def name(): #start takes no arguments to begin
	print "What is your name?"
	
	name = raw_input('> ')
	
	if not name.isalpha():
		print "My dear child, that is not a name! Let's try this again\n"
		start()
	else: 
		print "Nice to meet you %s" % name
		wandcore_question()
	return name

# 4. Announcing your house!
def your_house():
	print "\nDo you remember all your anwers?"
	print "Which one did you get most?"
	print "Number 1, 2, 3, 4 and 5, for when you didn't choose\none of the answers I offerd you."
	
	number = raw_input("> ")
	if number == "1":
		print "Congratulations! You are a Ravenclaw! The Grey Lady is so happy your\nare in her house!" 
	elif number == "2":
		print "Congratulations! You are a Hufflepuff! The Fat Friar is eager to\nmeet you!"
		end()
	elif number == "3":
		print "You're a Gryffindor! Look - Sir Nicholas de Mimsy-Porpington wants\nto congratulate you!" 
		end()
	elif number == "4":
		print "Without a doubt. You are a Slytherin! The Bloody Baron is eager to\nmake your acquaintance!" 
		end()
	elif number == "5":
		print "I cannot decide! You could be sorted into any House. It is now up\nto you to choose."
		end()
	else:
		print "Stop messing around! Are you sure you even want to attend Hogwarts?!"
		end()

# 3. Howler question:
def howler_question():
	print "\nThe third and last question is:"
	print "Why do you think your parents would send you a howler?"
	print "1. You cheated on OWLS with a self-answering pen"
	print "2. You sold everyone snort-tasting Bertie Botts beans"
	print "3. You bewitched a Slytherin - he had it comming! "
	print "4. I didn't do it!"
	print "Type a number or your answer:"
	
	choice = raw_input("> ")
	
	if choice == "1":
		print "Having good grades is not everything in life!"
		your_house()
	elif choice == "2":
		print "Hahaha that is very funny!"
		your_house()
	elif choice == "3":
		print "I understand the feud, but next time use your words!"
		your_house()
	elif choice == "4":
		print "Are you sure?"
		your_house()
	else:
		print "I've never heared someone getting a Howler for %s!" % choice
		your_house()

# 3. Favourite person question
def person_question():
	print "\nThe third and last question is:"
	print "Which charcter is your favourite?"
	print "1. Albus Dumbledore"
	print "2. Luna Lovegood"
	print "3. Hermione Granger"
	print "4. Severus Snape"
	print "\nType a number or another character:"
	
	choice = raw_input("> ")
	
	if choice == "1":
		print "A powerful and wise wizzard." 
		your_house()
	elif choice == "2":
		print "A free spirit."
		your_house()
	elif choice == "3":
		print "A loyal and intelligent witch."
		your_house()
	elif choice == "4":
		print "A cunning and secret hero."
		your_house()
	else:
		print "Yes, I can see why this is your favourite character!"
		your_house()

# 3. Pet question
def pet_question():
	print "\nThe third and last question is:"
	print "What would be your pet at Hogwarts?"
	print "1. Owl"
	print "2. Toad"
	print "3. Cat"
	print "4. No pets for me!"
	print "\nType a number or another answer:"
	
	choice = raw_input("> ")
	
	if choice == "1":
		print "You will always get your post on time!"
		your_house()
	elif choice == "2":
		print "Why? Just why?!"
		your_house()
	elif choice == "3":
		print "They are great company! I love kittens too!"
		your_house()
	elif choice == "4":
		print "Pets are not for everyone."
		your_house()
	else:
		print "I see. Well, that is your choice."
		your_house()


# 3. Dumbledore quote
def dumbledore_question():
	print "\nThe third and last question is:"
	print "Which one of these quotes was not said by Dumbledore?"
	print "1. After all this time. 'Always.'"
	print "2. Happiness can be found even in the\ndarkest of times if one remebers to turn on the light."
	print "3. It's the unknown we fear when we look upon death\nand darkness, nothing more."
	print "4. I solemly swear, that I am up to no good."
	print "\ntype a number."
	
	choice = raw_input("> ")
	
	if choice == "1":
		print "Very good! Prof Snape said that."
		your_house()
	elif choice == "2":
		print "No, Dumbledore said that. It is quite a hopeful quote."
		your_house()
	elif choice == "3":
		print  "No, Dumbledore said that. He is a very wise wizzard!"
		your_house()
	elif choice == "4":
		print "Very good! I see you are familiar with the Marauders Map!"
	else:
		print "Remember: You will lose house points for not answering questions!"
		your_house()
		
	
# 3. Deathly Hollows question
def deathlyhollows_question():
	print "\nMy second question to you is:"
	print "Which Deathly Hallow would you choose?"
	print "My second question to you is:"
	print "Which spell would you use to protect yourself in a duell?"
	print "1. The Invisibility Cloak!"
	print "2. The Resurrection Stone!"
	print "3. The Elder Wand!"
	print "4. All of them!"
	print "\Type a number or a different answer:"

	choice = raw_input("> ")
	
	if choice == "1":
		print "You will uncover a lot of secrets."
		your_house()
	elif choice == "2":
		print "I could recommend you a grief counsellor. The resurrection stone will\nnot help you heal."
		your_house()
	elif choice == "3":
		print  "With great power comes great responsibility!."
		your_house()
	elif choice == "4":
		print  "You are destined for greatness - hopefully it will not corrupt you."
		your_house()
	else:
		print "Very wise."
		your_house()
	
# 2. Spell question
def spell_question():
	print "\nMy second question to you is:"
	print "Which spell would you use to protect yourself in a duell?"
	print "1. Stupefy!"
	print "2. Protego!"
	print "3. Expelliarmus!"
	print "4. Crucio!"
	print "\nType a number or a different spell:"

	spell = raw_input("> ")
	
	if spell == "1":
		print "If the other person is stunned, he cannot fight. Clever"
		deathlyhollows_question()
	elif spell == "2":
		print "Defense is a good way to not get hurt."
		dumbledore_question()
	elif spell == "3":
		print  "You chose to disarm the other person and end the fight."
		pet_question()
	elif spell == "4":
		print "I hope you are joking or you are going straight to Askaban!"
		person_question()
	else:
		print "%s - you are thinking out of the box." % (spell)
		howler_question()
		
# 1. Career question
def career_question():
	print "\nMy second question to you is:"
	print "Where do you see yourself working after graduating from Hogwarts?"
	print "1. As a teacher at Hogwarts" 
	print "2. As a caretaker of Magic Creatures." 
	print "3. As Cursebreaker for Gringotts"
	print "4. In the Ministry of Magic"
	print "Or something else?"
	print "\nType a number or a different career path:"
	
	choice = raw_input("> ")
	
	if choice == "1":
		print "Dedicating your life to passing on knowlege is very admirable."
		deathlyhollows_question()
	elif choice == "2":
		print "They will thank you for it!"
		dumbledore_question()
	elif choice == "3":
		print  "That will be an adventurous life! But I hope you have a life insurance!"
		pet_question()
	elif choice == "4":
		print "You really could make a difference in the world working there!"
		person_question()
	else:
		print "You're right. Everyone has to find their own path in life. " % (choice)
		howler_question()

# 2. Saturday question
def saturday_question():
	print "My second question to you is:"
	print "Which place would you want to visit on a Saturday?"
	print " 1. The Hogwarts Library" 
	print " 2. The kitchens"
	print " 3. The Forbidden Forest"
	print " 4. The Room of Requirement"
	print "Or something else?"
	print "\nType a number or a different place:"
	
	choice = raw_input("> ")
	
	if choice == "1":
		print "Good choice. But remember the dark magics department is off limits!" 
		deathlyhollows_question()
	elif choice == "2":
		print "Good choice. The houseelves love visits from students."
		dumbledore_question()
	elif choice == "3":
		print  "Good choice. But look out for the Zentauri!"
		pet_question()
	elif choice == "4":
		print "Good choice. You can be anywhere you want."
		person_question()
	else:
		print "Good choice. I haven't been there myself yet" % (choice)
		howler_question()

	
# 2. Mirror question
def mirror_question():
	print "\nMy second question to you is:"
	print "What do you see when you look in the Mirror of Erised?"
	print "Do you see yourself knowledgeable above all?" 
	print "Do you see yourself surrounded by family?"
	print "Or perhaps you are holding the Triwizzard Cup?"
	print "Or is it raining galleons on you?"
	print "\nType a sentence:"
	
	desire = raw_input("> ")
	
	#looking for a particular key word in position
	if "galleons" in desire: 
		print "Thank you for trusting me with your deepest desire."
		print "I promise I won't tell anyone."
		deathlyhollows_question()
	elif "Triwizzard Cup" in desire:
		print "Thank you for trusting me with your deepest desire."
		print "I promise I won't tell anyone."
		dumbledore_question()
	elif "knowlegeable" in desire:
		print "Thank you for trusting me with your deepest desire."
		print "I promise I won't tell anyone."
		pet_question()
	elif "family" in desire:
		print "Thank you for trusting me with your deepest desire."
		print "I promise I won't tell anyone."
		person_question()
	else: 
		print "Thank you for trusting me with your deepest desire."
		print "I promise I won't tell anyone."
		howler_question()
	
	
# 2. Quidditch question
def quidditch_question(): 
	print "\nMy second question to you is:"
	print "If you could choose, which Quidditch position would you play?"
	print "If you don't remember, there are four position:"
	print "Seeker, Keeper, Chaser, Beater"
	print "\n type your position:"
	
	position = raw_input("> ")
	
	#looking for a particular key word in position
	if "Seeker" in position: 
		print "You like the glory, don't you." # ra
		deathlyhollows_question()
	elif "Keeper" in position:
		print "You truely have everyone's back." # hu
		person_question()
	elif "Chaser" in position:
		print "You seem to like working in a team." # gr
		pet_question()
	elif "Beater" in position:
		print "You seem to like power." # sl
		dumbledore_question()
	else: 
		print "If you say so..." # hu
		howler_question()


# 1. Wandcore question
def wandcore_question():
	print "\nI am going to ask you a couple of questions"
	print "to sort you into the correct house."
	print "Please remeber your three answers as we go along."
	print "What material is at the core of your wand?"
	print " 1. Mermaid Scales" # ra
	print " 2. Phoenix Feather" # hu
	print " 3. Dragon Heartsting" # gr
	print " 4. Unicorn Hair" # sl
	print "Or something else?" # hu
	print "\nType a number or the substance of wand's core:"
	
	wandcore = raw_input("> ")
	if wandcore == "1":
		print "Mermaids ... they are very intelligent creatures."
		quidditch_question()
	elif wandcore == "2":
		print "Phoenix you say ... they are very loyal."
		mirror_question()
	elif wandcore == "3":
		print  "Dragons ... very powerful creatures."
		saturday_question()
	elif wandcore == "4":
		print "Unicorns ... intersting."
		career_question()
	else:
		print "%s is a very unique core indeed." % (wandcore)
		spell_question()
		

def end():
	print "\nThe End"
	exit(0)

def start():
	print "You have received an acceptance letter from Hogwarts an are now attending the Sorting Ceremony."
	print "Hello, I am the sorting hat."
	name()

start()	# function start will run automatically