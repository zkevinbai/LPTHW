### I cannot get this to run, nor can i figure out the relationship
### between Scene, Engine and Map 

### Gothons from Planet Percal #25

class Scene(object):

    def enter(self):
        self.map()

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        print self.scene_map

class Death(Scene):

    def enter(self):
        print """Lucky for you, death is an inmaterial concept in video games,
        \ryou have died.  Try again!"""

class CentralCorridor(Scene):

    def enter(self):
        print """This is the starting point and has a Gothon already standing
        \rthere they have to defeat with a joke before continuing."""
        response = raw_input("Tell me a joke!")
        if isinstance(response, basestring):
            print "The Gothon laughs itself to death."
            self.next_scene("LaserWeaponArmory")
        else:
            self.Scene

class LaserWeaponArmory(Scene):

    def enter(self):
        print "pop"
        pass

class TheBridge(Scene):

    def enter(self):
        pass

class EscapePod(Scene):

    def enter(self):
        pass

class Map(object):

    def __init__(self, start_scene):
        current_scene =  self.start_scene
        self.

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        map.CentralCorridor()



a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
