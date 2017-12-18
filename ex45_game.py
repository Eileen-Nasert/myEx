print "ex45"
print "The Triwizard Tournament\n"

from sys import exit
from random import randint
import webbrowser

#
class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."
		exit(1)

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
				next_scene_name = current_scene.enter()
				current_scene = self.scene_map.next_scene(next_scene_name)
		current_scene.enter()


# last scene called death
class Death(Scene):
	quips = [
		"You kinda suck at magic. And are an embarrassment to Hogwarts! "
		"This must be the first time in History, that the Goblet of Fire made a "
		"mistake. Honestly, I have a small pigwidgeon that's better at this than you!"
		]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)
		
# end scene
class End(Scene):

	def enter(self):
		exit(1)

# first scene
class ChoosingCeremony(Scene):
		
	def enter(self):	
		print "You are sitting in the great Hall of Hogwarts and"
		print "are eagerly awaiting Dumbeldore's speech."
		print "\"Welcome students! This year Hogwarts will hold"
		print "the Triwizard Tournament. Eternal glory!"
		print "That's what awaits the victor,"
		print "but to do this, the champions must survive three tasks."
		print "The champion will be chosen by an impartial selector:"
		print "The Goblet of Fire!"
		print "Let me be clear. If chosen, you stand alone."
		print "If you dare, enter in your name, otherwise,"
		print " enter 'spectator' and watch the tournament unfold.\""
		
		global name 
		name = raw_input("> ")
		
		if name == "spectator":
			print "\"Wise choice - today will not the day you die.\""
			new=2;
			url="https://www.youtube.com/watch?v=VUQzN0lnxu8";
			webbrowser.open(url, new=new);
			return 'end'
		elif name == "shortcut":
			print "This is the short cut to the grave scene."
			return 'voldemort_grave'
		elif name.isdigit():
			print "\n\"My dear child, that is not a name! Let's try this again\"\n"
			return 'choosing_ceremony'
		elif name.isalpha():
			print "\"You are very brave, %s \"" % name
			return 'age_ring'
		else: 
			print "DOES NOT COMPUTE NAME!"
			return 'choosing_ceremony'
		
		
# age ring
class AgeRing(Scene):
	
	def enter(self):
		age = int(raw_input("Please enter your age\n> "))
		
		if age in range(17, 21):
			print "\"You have passed the Age Restriction line" 
			print "Oh see, the blue-white colored flames of the Goblet of Fire are"
			print "suddenly changing!\""
			print "In a rush of red flames it spits out a piece of parchment. The"
			print "name %s is written on it!" %name
			print "\"Congratulations %s, you are the Champion for Hogwarts!\"" %name
			return 'first_task'
		elif age in range(17):
			print "\"I am sorry to say, but you are too young to be a Champion."
			print "You must be at least 17 to pass the Age Line."
			print "Try your luck again at the next Tournament in five years.\""
			return 'end'
		elif age in range(21, 99):
			print "\"Aha! %s are caught using an Aging Potion!" %name
			print "As punishment you are growing a white long beard,"
			print "which you won't get rid of for two weeks!" 
			print "Try your luck again at the next Tournament in five years.\""
			return 'end'
		else: 
			print "DOES NOT COMPUTE AGE!"
			return 'age_ring'
		
# second Scene
class FirstTask(Scene):

	def enter(self):
		print "\"The first task is designed to test your daring. Courage in"
		print "the face of the unknown is an important quality in a wizard.\""
		print "But first you must choose a number: enter 1,2,3 or 4"
		
		choice = raw_input("number > ")

		if choice == "shortcut":
				print "This is the short cut to the grave scene."
				return 'voldemort_grave'
				
# Swedish Short-Snout		
		elif choice == "1":
			print "You have picked the Swedish Short-Snout!"
			print "Its scales are silvery blue, and its powerful flame"
			print "is also a brilliant blue color and hot enough to" 
			print "reduce timber and bone to ashes in seconds!"
			print "You must get the golden egg it's protecting."
			print "How do you get past the dragon?"
			print "1. You shout 'STUPIFY'."
			print "2. You use a transfiguration spell!"

			choice = raw_input("number > ")
	
			if choice == "1":
				print "Your plan to stun the dragon has not worked."
				print "Instead you have just made it angrier." 
				print "The dragon stomps you to death."
				return 'death'
			elif choice == "2":
				print "You have transfigured a stone into a dog."
				print "The dragon is distracted and you can snatch"
				print "the golden egg. You passed the first task!"
				return 'second_task'	
			else:
				print "DOES NOT COMPUTE!"
				return 'first_task'

#Common Green Welch
		elif choice == "2":
			print "You have picked the Common Green Welsh!"
			print "Its  scales are grass green and it has a distinctive"
			print "musical roar. But be aware of its thin jets of fire."
			print "They will be fatal!"
			print "You must get the golden egg it's protecting."
			print "How do you get past the dragon?"
			print "1. You use a sleeping spell!"
			print "2. You shout 'EXPELLIARMUS'"
		
			choice = raw_input("number> ")
			
			if choice == "1":
				print "The dragon stumbles a bit and falls asleep. However, right"
				print "before you snatch the egg a snore of fire light up your robe." 
				print "But you are lucky and can put out the fire in time. You" 
				print "have barely made it to the second task."
				return 'second_task'
			elif choice == "2":
				print "This was pretty stupid! A dragon can't be disarmed."
				print "instead you have provoked the dragon and devours you whole."
				return 'death'
			else:
				print "DOES NOT COMPUTE!"
				return 'first_task'

#Chinese Fireball 
		elif choice == "3":
			print "You have picked the Chinese Fireball!"
			print "The dragon has scarlet colored scales, yellow eyes and"
			print "was named for the brilliant deadly rounded balls of fire"
			print "that it shoots from its nostrils. "
			print "You must get the golden egg it's protecting."
			print "How do you get past the dragon?"
			print "1. You use the Conjunctivtis curse!"
			print "2. You shout 'ACCIO golden egg!'."
		
			choice = raw_input("number > ")
			
			if choice == "1":
				print "You have blinded the dragon with the curse. However, it stumbels"
				print "over a rock and almost buries you underneath it's belly." 
				print "Yet, you can jump aside at the last second and snatch the"
				print "golden egg. You've made it to the next round!"
				return 'second_task'
			elif choice == "2":
				print "Sadly, the golden egg doesn't move an inch, because it is"
				print "protected by an anti-accio spell. In a moment of"
				print "inattentiveness, the dragon whacks you with it's tale and"
				print "you are impaled by the spikes and die."
				return 'death'
			else:
				print "DOES NOT COMPUTE!"
				return 'first_task'

#Hungarian Horntail
		elif choice == "4":
			print "You have picked the Hungarian Horntail! It has black scales, bronze" 
			print "horns and spikes. Be cautious! It has the longest fire-breathing range"
			print "of all dragons, which can't be put out wiht water."
			print "You must get the golden egg it's protecting."
			print "How do you get past the dragon?"
			print "1. You shout 'Sectum Sempra!'"
			print "2. You scream 'Accio Firebolt!'"
		
			choice = raw_input("number > ")
		
			if choice == "1":
				print "This spell created by the Halfblood Prince only works on humans!"
				print "The leather skin of dragons can't be so easily cut. The dragon"
				print "becomes furious and bombards you with fire breath."
				print "You try to escape, but it's long breath of fire catches you"
				print "And you die a horrible death, slowly burning to ashes."
				return 'death'
			elif choice == "2":
				print "Your broomstick flies in your hand, you jump on it and can dodge"
				print "every single fire breath. You are too fast for the dragon and"
				print "can easily snatch the golden egg Well done!"
				print "You've made it to the second round!"
				return 'second_task'
			else:
				print "DOES NOT COMPUTE!"
				return 'first_task'

		else:
			print "DOES NOT COMPUTE!"
			return 'first_task'

# third scene
class SecondTask(Scene):

	def enter(self):
		print "You have managed to open the golden egg and hear a clue" 
		print "for the second task." 
		print "\"Come seek us where our voices sound,"
		print "We cannot sing above the ground,"
		print "And while you're searching, ponder this;"
		print "We've taken what you'll sorely miss,"
		print "An hour long you'll have to look,"
		print "And recover what we took,"
		print "But past an hour, the prospect's black,"
		print "Too late, it's gone, it won't come back.\""
		print "How will you breathe under water?"
		print "1. I use the Bubble-Head Charm."
		print "2. I will partially transfigure myself into a shark."
		print "3. I will eat gillyweed."
		
		choice = raw_input("number > ")
		
		if choice == "1":
			print "This charm creates an air-bubble around your mouth."
			print "However, your vision is blurred under water and"
			print "suddenly a grindylow attacks you and bursts your bubble."
			print "You panic, your foot gets stuck in sea tang and you drown."
			return 'death'
		elif choice == "2":
			print "Your transformation was successful and you were able to"
			print "save your loved one. But you accidentally bit of an arm."
			print "You completed the second round, but your loved one,"
			print "hexes you and with a spell, that turn your insides out."
			print "You die an agonizing death before you before you can make"
			print "it to the third round."
			return 'death'
		elif choice == "3":
			print "You grow gills and webbing between fingers and toes and"
			print "have no problem breathing under water and save your loved one."
			print "Thus, you've made it to the third and final round!"
			return 'third_task'
		else:
			print "DOES NOT COMPUTE!"
			return 'second_task'
			
# fourth scene 
class ThirdTask(Scene):

	def enter(self):
		print "\"You are finally here. The third round!"
		print "Whoever finds the cup first in the maze, wins the tournament"
		print "but be careful, you might lose yourself along the way.\""
		print "You enter the maze. Do you choose left, right, or the path straight ahead?"

		choice = raw_input("direction > ")
	
# left Sphinx	
		if choice == "left":
			print "You encounter a Sphinx. She has the body of a lion and the head of"
			print "a woman. She will let you pass if you solve a riddle."
			print "\"First think of the person who lives in disguise,"
			print "Who deals in secrets and tells naught but lies."
			print "Next, tell me what's always the last thing to mend,"
			print "The middle of middle and end of the end?"
			print "And finally give me the sound often heard,"
			print "During the search for a hard-to-find word."
			print "Now string them together and answer me this,"
			print "Which creature would you be unwilling to kiss?\""
			
			choice = raw_input("word > ")
			
			if choice == "spider":
				print "You are very clever - you're probably a Rawenclaw."
				print "You have earned your save passage. Good luck."
				return 'cup_scene'
			else:
				print "The sphinx attacks you with its paws and slices your throat."
				print "As you lay there bleeding out, you realize the answer was 'spider'."
				print "You slowly fade away and die."
				return 'death'
				
# right Blast-Ended Screwt
		elif choice == "right":
			print "You encounter a Blast-Ended Screwt, which have a mean sting and squirt"
			print "fire. Suddenly, the maze closes your escape route behind you." 
			print "The only way out is to get past the monster."
			print "What do you do?"
			print "1. I use the Impediment Jix!"
			print "2. I scream Acqua Eructo!"
			
			choice = raw_input("number > ")
			
			if choice == "1":
				print "Very clever. You used a spell, which can freeze magical beasts"
				print "for about ten seconds. Now hurry up and run past the Screwt!"
				return 'cup_scene'
			elif choice == "2":
				print "You spray water at the Screwt and it slows down. You think it"
				print "save to run past the best, when you suddenly feel a sting"
				print "piercing your back. The venom spreads through your veins, "
				print "paralyzing you. You can't lift your wand to send a distress signal"
				print "and you slowly die while the Screwt is munching you flesh."
				return 'death'
			else:
				print "DOES NOT COMPUTE, type in left, right, or straight ahead!"
				return 'third_task'
				
# straight ahead Dementor/Boggart
		elif "straight ahead" in choice:
			print "As you are walking, suddenly, the air around you becomes cold and" 
			print "you see a hooded figure floating toward you. It looks likes" 
			print "a dementor, but you don't want to get close enough to be certain."
			print "Which spell do you use??"
			print "1. I scream 'Expecto Patronum'!"
			print "2. I scream 'Riddikulus!'"
		
		
			choice = raw_input("number > ")
			
			if choice == "1":
				print "If you would have paid attention in Defense Against the"
				print "Dark Arts, you would have known, that this is not"
				print "a dementor, but a Boggart. The Boggart senses your fear and"
				print "keeps changing into other things from your worst nightmares!"
				print "You have a mental breakdown and have to leave the maze in shame."
				return 'end'
			elif choice == "2":
				print "Ah you've paid attention in Defense Against the Dark Arts!"
				print "Indeed, this is not a dementor but a boggart."
				print "You've the defeated the boggart easily and can run past it."
				return 'cup_scene'
			else:
				print "DOES NOT COMPUTE!"
				return 'third_task'
		else:
			print "DOES NOT COMPUTE!"
			return 'third_task'

# fifth scene
class CupScene(Scene):

	def enter(self):
		print "You have almost made it. You know you are close. You have one final" 
		print "decision to make."
		
# 		good_path = randint(1,5)
# 		good_path = 3
		print "Which path of 5 do you choose?"
		
		guess = raw_input("path number > ")
		
# 		elif int(guess) != good_path:
		if guess == "3":
			print "You're lucky and guessed correctly!"
			print "Did you perhaps drink a drop of Felix Felicis? ;) "
			return 'voldemort_grave'
		else:	
			print "You have guessed %s and get lost in the maze and lose." %guess
			return 'end'	

# sixth scene 
class VoldemortGrave(Scene):
	global name
	def enter(self):
		
		print "Finally you see the Triwizzard cup at the end of the path and you run"
		print "towards it. Filled with joy of victory you pick up the cup. You've won"
		print "the tournament! Suddenly, you feel a strange sensation as you spin around"
		print "faster and faster. The cup is a portkey!! Then the movement stopps and"
		print "you find yourself in a graveyard, far away from the maze and Hogwarts."
		print "Is this still part of the tournament? In that moment, several Deatheater"
		print "apprate around you and have you surrounded. One man steps forward and" 
		print "reveals it's ugly mouse-like face man. It is Peter Pettigrew!"
		
		if name != "Harry":
			print "Sadly you are not the Chosen one."
			print "Before you can pull out you wand and defend yourself. Pettigrew"
			print "screams Avada Kedavra and you fall to ground. Dead in an instance."
			return 'end'
		
		else:
			print "Before you can pull out your wand and defend yourself. Pettigrew"
			print "slices your arm and drops your blood in a cauldron, while saying:"
			print "\"Blood of the enemy, forcibly taken, you will resurrect your foe\""
			print "The fluid inside the cauldron fuzzes and bubbles,"
			print "when all of a sudden the surface becomes completely"
			print "calm as a figure slowly emerges from within."
			print "It is Lord Voldemort!"
			print "\"Hello Harry Potter and so we meet once more. But today will" 
			print "be the last time. However, I will not simply kill you,"
			print "but defeat you in a duell! Pick up your wand at fight!\""
			print "What do you do?"
			print "1. Yell 'Expelliarmus!'"
			print "2. Yell 'Protego!'"
			
			choice = raw_input("number > ")
			
			if choice == "1":
				print "You tried to disarm Lord Voldemort and although, he still holds"
				print "his wand, you threw him out of balance for a moment."
				print "You use his hesitation to grab the cup, which transports you"
				print "back to Hogwarts. You've escaped Lord Voldemort and can warn"
				print "everyone, that he is back. You have not just won the"
				print "tournament, but you also helped win the war against" 
				print "the Deatheaters! You are a Champion and true hero!"				
				return 'end'
			elif choice == "2":
				print "You've created a force shield, but Voldemort's unforgivable curse"
				print "is too strong and catapults you with your force shield backwards."
				print "You bang your head against a gravestone and are knocked"
				print "unconsious. You wake up to Voldemort toruring you with the"
				print "Cruciatus curse. Eventually he gets bored of it though and let's"
				print "Nagini eats you. The Dark Lord has risen once more."
				return 'end'
			else:
				print "DOES NOT COMPUTE!"
				return 'third_task'
	
# creating a dict called scenes
class Map(object):
	
	scenes = {
		'choosing_ceremony': ChoosingCeremony(),
		'age_ring' : AgeRing(),
		'first_task': FirstTask(),
		'second_task': SecondTask(),
		'third_task': ThirdTask(),
		'cup_scene': CupScene(),
		'voldemort_grave': VoldemortGrave(),
		'death': Death(),
		'end': End()
		}
		
	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name) # referring to dict with map.scenes
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

# let the game begin
a_map = Map('choosing_ceremony')
a_game = Engine(a_map)
a_game.play()

