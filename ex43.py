print "ex 43 - Gothons Game Engine\n"
# basic imports for game
from sys import exit
from random import randint


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
		"I guess you're dead. You kinda suck at this."
		"I guess you'll never live up to the expacations of yourself."
		"I have a small cat that's better at this! LOL"
		]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)

# first scene called central corridor
class CentralCorridor(Scene):

	def enter(self):
		print "balabala something happens to you and you must take action"
		
		action = raw_input("> ")
		
		if action == "shoot!":
			print "balaba whatever happens to you when you shot"
			return 'death'
		
		elif action == "dodge!":
			print "balababa"
			return 'death'
		
		elif action == "tell a joke":
			print "blahblah"
			return 'laser_weapon_armory'
		
		else:
			print "DOES NOT COMPUTE!"
			return 'central_corridor'

# second room
class LaserWeaponArmory(Scene):

	def enter(self):
		print "Guess a three-digit code to open door - if you get it worng 10 times, it will close forever"
		code = "%d%d%d" %(randint(1,9), randint(1,9), randint(1,9)) #random numbers between 1 and 9 imported from sys random 
		guess = raw_input("[keypad]> ")
		guesses = 0
		
		while guess != code and guesses <9:
			print "BZZZZEDD"
			guesses += 1 # increment
			guess = raw_input("[keypad]>")
		
		if guess == code:
			print "blabla you've made it to the bridge."
			return 'the_bridge'
		else:
			print "balba lock is now forever cealled."
			print "wating for a gothon to find you"
			return 'death'
			
# third room
class TheBridge(Scene):

	def enter(self):
		print " something exciting happens, what do you do?"
		
		action = raw_input("> ")
		
		if action == "throw the bomb":
			print "balaba"
			return 'death'
		
		elif action == "place the bomb":
			print "balaba"
			return 'escape_pod'
		else:
			print "DOES NOT COMPUTE!"
			return 'the_bridge'

# fourth room
class EscapePod(Scene):

	def enter(self):
		good_pod = randint(1,5)
		print "Which escape pod do you use?"
		
		guess = raw_input("[pod #]> ")
		
		if int(guess) != good_pod:
			print "You have guessed %s and die" %guess
			return 'death'
		else:
			print "You jump onto pod %s and live!!" %guess
			return 'finished'

# last scene

class Finished(Scene):

	def enter(self):
		print "you won! Good job."
		return 'finished'
	
# 
class Map(object):
	#creating a dict called scenes
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon-armory': LaserWeaponArmory(),
		'the_bridge': TheBridge(),
		'escape_pod': EscapePod(),
		'death': Death(),
		'finished': Finished()
		}
		
	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name) # referring to dict with map.scenes
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)

# let the games begin
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()






