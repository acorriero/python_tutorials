from sys import exit
from random import randint

class Scene(object):
    def __init__(self):
        pass

    def enter(self):
        print "Scene isn't implemented yet. Subclass it and implement enter()"
        exit(1)

    def death(self):
        print "You die!"
        exit(0)

    def central_corridor(self):
        print "What would you like to do?"
        print "shoot, dodge, or tell a joke"

        action = raw_input("> ")

        if action == "shoot":
            print "He stomps you."
            return 'death'

        elif action == "dodge":
            print "He eats you."
            return 'death'

        elif action == "tell a joke":
            print "You put him down."
            return 'laser_weapon_armory'

        else:
            print "DOES NOT COMPUTE!"
            return 'central_corridor'
            
        if self.scene == "death":
            self.death()
        elif self.scene == "central_corridor":
            self.central_corridor()
        elif self.scene == "laser_weapon_armory":
            self.laser_weapon_armory()
        elif self.scene == "the_bridge":
            self.the_bridge()
            
    def laser_weapon_armory(self):
        print "You dive roll into the armory?"
        code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        guess = raw_input("[keypad]> ")
        guesses = 0
        
        while guess != code and guesses < 10:
            print "bzzzzzzd"
            guesses += 1
            guess = raw_input("[keypad]> ")
        if guess == code:
            print "You got it!"
            return "the_bridge"
        else:
            print "you missed your chance"
            return "death"

    def the_bridge(self):
        pass
    
    def escape_pod(self):
        pass

class Engine(object):
 
    scenes = {
              'central_corridor': central_corrirdor(),
              'laser_weapon_armory': LaserWeaponArmory(),
              'the_bridge': TheBridge(),
              'escape_pod': EscapePod(),
              'death': Death()
    }
 
    def __init__(self, scene):
        self.scene = scene
     
    def next_scene(self):
        return Engine.scenes['scene']
    

#a_map = Map('central_corridor')
#a_game = Engine(a_map)
#a_game.play()

a_game = Scene()
status = a_game.central_corridor()

while True:
    print "\n--------"
    next_scene_name = self.scene_object.scene()
    current_scene = self.scene_map.next_scene(next_scene_name)