class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)


# Scene 1 Choosing Ceremony
choosing_ceremony = Scene("Choosing Ceremony", "choosing_ceremony",
"""
You are sitting in the great Hall of Hogwarts and
are eagerly awaiting Dumbeldore's speech:
Welcome students! This year Hogwarts will hold the Triwizard Tournament.
Eternal glory! - That is what awaits the victor ... but first the Champions must
survive the three tasks. The Champions will be choosen by an impartial selector.
The Goblet of Fire! Let me be clear - if chosen, you stand alone.
If you dare, enter your age:
""")

# Scene 2A Age Ring: Life
age_ring_life = Scene("Choosing Ceremony", "age_ring_life",
"""
You have passed the Age Restriction line. Oh see, the blue-white colored
flames of the Goblet of Fire are suddenly changing!
In a rush of red flames it spits out a piece of parchment with your name written
on it. Congratulations, you are the Champion for Hogwarts!
""")

# Scene 2B Age Ring: Death
age_ring_death = Scene("Choosing Ceremony", "age_ring_death",
"""
You are caught using an Aging Potion!
As punishment you are growing a white long beard, which you won't get rid
of for two weeks! Try your luck again at the next tournament in five years.
""")

# Scene 3 First Task Arena
first_task = Scene("Arena", "first_task",
"""
The first task is designed to test your daring. Courage in the face of the
unknown is an important quality in a wizard.
But first you must choose a number: [Enter 1, 2, 3 or 4]
""")

# Scene 3.1 First Task Dragon 1
first_dragon = Scene("Arena", "first_dragon",
"""
You have picked the Swedish Short-Snout!
Its scales are silvery blue, and its powerful flame is also a brilliant
blue color and hot enough to reduce timber and bone to ashes in seconds!
You must get the golden egg it's protecting. How do you get past the dragon?
You shout STUPIFY!: [Enter 1] You use a transfiguration spell! : [Enter 2]
""")

# Scene 3.1A First Task Dragon 1: Enter 2 Life
first_dragon_life = Scene("Arena", "first_dragon_life",
"""
You have transfigured a stone into a dog. The dragon is distracted and you
can snatch the golden egg. You passed the first task!"
""")

# Scene 3.1B First Task Dragon 1: Enter 1 Death
first_dragon_death = Scene("Arena", "first_dragon_death",
"""
Your plan to stun the dragon has not worked. Instead you have just made
it angrier. The dragon stomps you to death.
""")

# Scene 3.2 First Task Dragon 2
second_dragon = Scene("Arena", "second_dragon",
"""
You have picked the Common Green Welsh!
Its  scales are grass green and it has a distinctive musical roar. But be
aware of its thin jets of fire. They will be fatal! You must get the golden
egg it's protecting. How do you get past the dragon?"
You use a sleeping spell! [Enter 1] You shout EXPELLIARMUS! [Enter 2]
""")

# Scene 3.2A First Task Dragon 2: Enter 1 Life
second_dragon_life = Scene("Arena", "second_dragon_life",
"""
The dragon stumbles a bit and falls asleep. However, right before you
snatch the egg a snore of fire light up your robe. But you are lucky and
can put out the fire in time. You have barely made it to the second task.
""")

# Scene 3.2B First Task Dragon 2: Enter 2 Death
second_dragon_death = Scene("Arena", "second_dragon_death",
"""
This was pretty stupid! A dragon can't be disarmed. Instead you have provoked
the dragon and devours you whole.
""")

# Scene 3.3 First Task Dragon 3
third_dragon = Scene("Arena", "third_dragon",
"""
You have picked the Chinese Fireball! The dragon has scarlet colored scales,
yellow eyes and was named for the brilliant deadly rounded balls of fire
that it shoots from its nostrils. You must get the golden egg it's protecting.
How do you get past the dragon? You use the Conjunctivtis curse! [Enter 1]
You shout ACCIO golden egg! [Enter 2]
""")

# Scene 3.3A First Task Dragon 3: Enter 1 Life
third_dragon_life = Scene("Arena", "third_dragon_life",
"""
You have blinded the dragon with the curse. However, it stumbels over a rock and
almost buries you underneath it's belly.Yet, you can jump aside at the last
second and snatch the golden egg. You've made it to the next round!
""")

# Scene 3.3B First Task Dragon 3: Enter 2 Death
third_dragon_death = Scene("Arena", "third_dragon_death",
"""
Sadly, the golden egg doesn't move an inch, because it is protected by an
anti-accio spell. In a moment of inattentiveness, the dragon whacks you with
it's tale and you are impaled by the spikes and die.
""")

# Scene 3.4 First Task Dragon 4
fourth_dragon = Scene("Arena", "fourth_dragon",
"""
You have picked the Hungarian Horntail! It has black scales, bronze horns and
spikes. Be cautious! It has the longest fire-breathing range of all dragons,
which can't be put out wiht water. You must get the golden egg it's protecting.
How do you get past the dragon? You shout Sectum Sempra! [Enter 1] You scream
Accio Firebolt! [Enter 2]
""")

# Scene 3.4A First Task Dragon 4 Enter 1 Death
fourth_dragon_death = Scene("Arena", "fourth_dragon_death",
"""
This spell created by the Halfblood Prince only works on humans! The leather
skin of dragons can't be so easily cut. The dragon becomes furious and bombards
you with fire breath. You try to escape, but it's long breath of fire catches
you and you die a horrible death, slowly burning to ashes.
""")

# Scene 3.4B First Task Dragon 4 Enter 2 Life
fourth_dragon_life = Scene("Arena", "fourth_dragon_life",
"""
Your broomstick flies in your hand, you jump on it and can dodge every single
fire breath. You are too fast for the dragon and can easily snatch the golden
egg Well done! You've made it to the second round!
""")

# Scene 4 Second Task Lake
second_task = Scene("Lake", "second_task",
"""
You have managed to open the golden egg and hear a clue for the second task.
"Come seek us where our voices sound,
We cannot sing above the ground,
And while you're searching, ponder this;
We've taken what you'll sorely miss,
An hour long you'll have to look,
And recover what we took,
But past an hour, the prospect's black,
Too late, it's gone, it won't come back."
How will you breathe under water?
I use the Bubble-Head Charm. [Enter 1] I will eat gillyweed. [Enter 2] I will
partially transfigure myself into a shark [Enter 3]
""")

# Scene 4A Second Task: Enter 1 Death
lake_death_1  = Scene("Lake", "lake_death_1",
"""
This charm creates an air-bubble around your mouth. However, your vision
is blurred under water and suddenly a grindylow attacks you and
bursts your bubble. You panic, your foot gets stuck in sea tang and you drown.
""")

# Scene 4A Second Task: Enter 3 Death
lake_death_2  = Scene("Lake", "lake_death_2",
"""
Your transformation was successful and you were able to save your loved one. But
you accidentally bit of an arm. You completed the second round, but your loved
one, hexes you and with a spell, that turn your insides out. You die an
agonizing death before you before you can make it to the third round.
""")

# Scene 4B Second Task: Enter 2 Life
lake_life  = Scene("Lake", "lake_life",
"""
You grow gills and webbing between fingers and toes and have no problem
breathing under water and save your loved one. Thus, you've made it
to the third and final round!
""")

# Scene 5 Third Task: Maze
third_task = Scene("Maze", "third_task",
"""
You are finally here. The third round! Whoever finds the cup first in the
maze, wins the tournament but be careful, you might lose yourself along the way.
You enter the maze.
Do you choose left: [Enter left] Or do you choose right: [Enter right]
""")

# Scene 5.1 Third Task: Enter  Left
sphinx_path = Scene("Maze", "sphinx_path",
"""
You encounter a Sphinx. She has the body of a lion and the head of a woman.
She will let you pass if you solve a riddle:
First think of the person who lives in disguise,
Who deals in secrets and tells naught but lies.
Next, tell me what's always the last thing to mend,
The middle of middle and end of the end?
And finally give me the sound often heard,
During the search for a hard-to-find word.
Now string them together and answer me this,
Which creature would you be unwilling to kiss?
Enter your answer
""")

# Scene 5.1A Sphinx Answer Right: Life
sphinx_life = Scene("Maze", "sphinx-life",
"""You are very clever - you're probably a Rawenclaw.
You have earned your save passage. Good luck.
""")

# Scene 5.1B Sphinx Answer Wrong: Death
sphinx_death = Scene("Maze", "sphinx-death",
"""
The sphinx attacks you with its paws and slices your throat.
As you lay there bleeding out, you realize the answer was 'spider'.
You slowly fade away and die.
""")

# Scene 5.2 Third Task: Enter 2 Right
dementor_path =Scene("Maze", "dementor_path",
"""
As you are walking, suddenly, the air around you becomes cold and you see a
hooded figure floating toward you. It looks likes a dementor, but you don't
want to get close enough to be certain. Which spell do you use??"
You scream Expecto Patronum! [Enter: 1]
You scream Riddikulus! [Enter: 2]
""")

# Scene 5.2A Third Task: Enter 2 Right
dementor_death = Scene("Maze", "dementor_death",
"""
If you would have paid attention in Defense Against the Dark Arts, you would
have known, that this is not a dementor, but a Boggart. The Boggart senses
your fear and keeps changing into other things from your worst nightmares!
You have a mental breakdown and have to leave the maze in shame.
""")

# Scene 5.2B Third Task: Enter 2 Right
dementor_life = Scene("Maze", "dementor_life",
"""
Ah, you've paid attention in Defense Against the Dark Arts! Indeed, you are not
facing a dementor but a boggart!
Thus, you've the defeated the boggart easily and can run past it.
""")

# Scene 6 Cup Scene
cup_scene = Scene("Maze", "cup_scene",
"""
Finally you see the Triwizzard cup at the end of the path and you run
towards it. Filled with joy of victory you pick up the cup. You've won
the tournament! Suddenly, you feel a strange sensation as you spin around
faster and faster. The cup is a portkey!! Then the movement stops and
you find yourself in a graveyard, far away from the maze and Hogwarts.
""")


# Scene 7 Graveyard Scene
graveyard_scene = Scene("Graveyard", "graveyard_scene",
"""
Is this still part of the tournament? In that moment, several Deatheaters
apprate around you and have you surrounded. One man emerges from the dark.
It's Lord Voldemort!
Lord Voldemort suddenly raises his wand. What do you do?
You yell Expelliarmus! [Enter: 1] You yell Protego! [Enter: 2]
""")

# Scene 7A Graveyard Scene Enter 1: Life
graveyard_life = Scene("Graveyard", "graveyard_life",
"""
You tried to disarm Lord Voldemort and although, he still holds his wand, you
threw him out of balance for a moment.You use his hesitation to grab the cup,
which transports you back to Hogwarts. You've escaped Lord Voldemort and can
warn everyone, that he is back. You have not just won the tournament, but you
also helped win the war against the Deatheaters!
You are a Champion and true hero!
""")

# Scene 7B Graveyard Scene Enter 1: Death
graveyard_death = Scene("Graveyard", "graveyard_death",
"""
You've created a force shield, but Voldemort's unforgivable curse is too strong
and catapults you with your force shield backwards. You bang your head against
a gravestone and are knocked unconsious. You wake up to Voldemort toruring you
with the Cruciatus curse. Eventually he gets bored of it though and let's Nagini
eats you.
The Dark Lord has risen once more.
""")


# Paths:
choosing_ceremony.add_paths({
    '16': age_ring_life,
    '17': age_ring_life,
    '18': age_ring_life,
    '*':  age_ring_death,
    # Shortcuts:
    'lake' : second_task,
    'maze' : third_task,
    'cup' : cup_scene,
    'grave' : graveyard_scene
})

age_ring_life.add_paths({
    '*':  first_task
})

first_task.add_paths({
    '1': first_dragon,
    '2': second_dragon,
    '3': third_dragon,
    '4': fourth_dragon
})

first_dragon.add_paths({
    '*': first_dragon_death,
    '2': first_dragon_life
})

first_dragon_life.add_paths({
    '*': second_task
})

second_dragon.add_paths({
    '*': second_dragon_death,
    '2': second_dragon_life
})

second_dragon_life.add_paths({
    '*': second_task
})

third_dragon.add_paths({
    '*': third_dragon_death,
    '1' : third_dragon_life,
})

third_dragon_life.add_paths({
    '*': second_task
})

fourth_dragon.add_paths({
    '*': fourth_dragon_death,
    '2' : fourth_dragon_life,
})

fourth_dragon_life.add_paths({
    '*': second_task
})

second_task.add_paths({
    '*': lake_death_1,
    '*': lake_death_2,
    '2': lake_life
})

lake_life.add_paths({
    '*': third_task
})

third_task.add_paths({
    'left': sphinx_path,
    'Left': sphinx_path,
    'right': dementor_path,
    'Right': dementor_path
})

sphinx_path.add_paths({
    'Spider': sphinx_life,
    'spider': sphinx_life,
    'Spyder': sphinx_life,
    'spyder': sphinx_life,
    '*': sphinx_death
})

sphinx_life.add_paths({
    '*' : cup_scene
})

dementor_path.add_paths({
    '2': dementor_life,
    '*': dementor_death
})

dementor_life.add_paths({
    '*' : cup_scene
})

cup_scene.add_paths({
    '*' : graveyard_scene
})

graveyard_scene.add_paths({
    '1': graveyard_life,
    '*': graveyard_death
})


SCENES = {
    choosing_ceremony.urlname : choosing_ceremony,
    age_ring_life.urlname : age_ring_life,
    age_ring_death.urlname : age_ring_death,
    first_task.urlname : first_task,
    first_dragon.urlname : first_dragon,
    first_dragon_life.urlname : first_dragon_life,
    first_dragon_death.urlname : first_dragon_death,
    second_dragon.urlname : second_dragon,
    second_dragon_life.urlname : second_dragon_life,
    second_dragon_death.urlname : second_dragon_death,
    third_dragon.urlname : third_dragon,
    third_dragon_life.urlname : third_dragon_life,
    third_dragon_death.urlname : third_dragon_death,
    fourth_dragon.urlname : fourth_dragon,
    fourth_dragon_life.urlname : fourth_dragon_life,
    fourth_dragon_death.urlname : fourth_dragon_death,
    second_task.urlname : second_task,
    lake_death_1.urlname : lake_death_1,
    lake_death_2.urlname : lake_death_2,
    lake_life.urlname : lake_life,
    third_task.urlname : third_task,
    sphinx_path.urlname : sphinx_path,
    sphinx_life.urlname : sphinx_life,
    sphinx_death.urlname : sphinx_death,
    dementor_path.urlname : dementor_path,
    dementor_death.urlname : dementor_death,
    dementor_life.urlname : dementor_life,
    cup_scene.urlname : cup_scene,
    graveyard_scene.urlname : graveyard_scene,
    graveyard_life.urlname : graveyard_life,
    graveyard_death.urlname : graveyard_death,
}
START = choosing_ceremony