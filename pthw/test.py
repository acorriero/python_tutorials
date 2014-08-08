class Map(object):
    def __init__(self,start_scene):
        self.start_scene = start_scene
        print "Start scene is: %s" % start_scene 
    
    def next_scene(self, scene_name):
        #self.scene_name = scene_name
        print "Scene name: %s" % scene_name
    
    def opening_scene(self):
        print "This is the opening scene."
        print self.start_scene

class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map
    
    def play(self):
        self.scene_map.opening_scene()
        

a_map = Map("Central Map")
g_start = Engine(a_map)
g_start.play()