# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# a starting process to solve OOP problem.

# Steps:

# 1. write or draw about the problem
# 2. Extract key concepts from #! and research them
# 3. Create a class hierarchy and object map for the concepts.
# 4. Code the classes and a test to run them.
# 5. Repeat and refine.

# list all nouns and verbs in writings and drawings and how they related
# nouns --> classes, objects, find out common parents
# verbs --> functions
# reduce the problems into a simple tree diagram
# write the skeleton code which has classes, functions
# write test to test the skeleton

class Map(object):

    def __init__(self,start_scene):
        print "You are at %s" % start_scene
    def next_scene(self,scene_name):
        print "You now enter %s." % scene_name
    def opening_scene(self):
        print "You are playing the game."

class Engine(object):
    def __init__(self,scene_map):
        print "Let's start the game engine!"

    def play(self):
        pass



class Scene(object):
    def enter(self):
        print "You now enter...." % self.enter()


class Death(Scene):
    def enter(self):
        print "You are dead now!"

class CentralCorridor(Scene):
    def enter(self):
        print "You are at the central corridor!"

class LaserWeaponArmory(Scene):
    def enter(self):
        print "You are passing the Laser Weapon Armory!"

class TheBridge(Scene):
    def enter(self):
        print "You are at the bridge now."

class EscapePod(Scene):
    def enter(self):
        print "Yes, you are inside of Escape Pod, Launch!"

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
