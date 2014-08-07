from sys import exit
from random import randint

class Scene(object):

    def enter(self):
        print "This scene is not yet configured. Subclass it and implement enter()."
        exit(1)

class Engine(object):

    def __init__(self, scene_map):
        print "Engine __init__ has scene_map", scene_map
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        print "Play's first scene", current_scene

        while True:
            print "\n--------"
            next_scene_name = current_scene.enter()
            print "next scene", next_scene_name
            current_scene = self.scene_map.next_scene(next_scene_name)
            print "map returns new scene", current_scene

class Death(Scene):

    quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
        print Death.quips[randint(0, len(Death.quips)-1)]
        exit(1)
class CentralCorridor(Scene):

    def enter(self):
        print "You've entered the central corridor."
        print "shoot, dodge, or tell a joke"

        action = raw_input("> ")

        if action == "shoot":
            print "He eats you."
            return 'death'

        elif action == "dodge":
            print "He stomps you"
            return 'death'

        elif action == "tell a joke":
            print "You enter the weapon armory."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print "The code is 3 digits."
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        print "The code is: %s" % code
        guess = raw_input("[keypad]> ")
        guesses = 1

        while guess != code and guesses < 3:
            print "BZZZZEDDD!"
            guesses += 1
            guess = raw_input("[keypad]> ")

        if guess == code:
            print "Good job"
            return 'the_bridge'
        else:
            print "You can't read numbers."
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print "You're at the bridge."
        print "Do you: throw a bomb or slowly place the bomb?"

        action = raw_input("> ")

        if action == "throw the bomb":
            print "It goes off."
            return 'death'

        elif action == "slowly place the bomb":
            print "Smart move."
            return 'escape_pod'
        else:
            print "DOES NOT COMPUTE!"
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print "Which escape pod?"
        print "1, 2, 3, 4, or 5" 

        good_pod = randint(1,5)
        print "Answer is: %d" % good_pod
        guess = raw_input("[pod #]> ")


        if int(guess) != good_pod:
            print "You jump into pod %s and hit the eject button." % guess
            return 'death'
        else:
            print "You jump into pod %s and hit the eject button." % guess
            print "You won!"
            return 'finished'

class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        print "start_scene in __init__", self.start_scene

    def next_scene(self, scene_name):
        print "start_scene in next_scene"
        val = Map.scenes.get(scene_name)
        print "next_scene returns", val
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)
    
a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
