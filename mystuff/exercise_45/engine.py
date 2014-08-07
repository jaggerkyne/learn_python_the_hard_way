# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from mystuff.exercise_45.scenes.death import Death
from mystuff.exercise_45.scenes.gold_room import GoldRoom
from mystuff.exercise_45.scenes.panda_room import PandaRoom
from mystuff.exercise_45.scenes.koi_pond_room import KoiPondRoom
from mystuff.exercise_45.scenes.bear_room import BearRoom
from mystuff.exercise_45.scenes.bat_room import BatRoom
from mystuff.exercise_45.scenes.win import Win
from mystuff.exercise_45.scenes.hall_of_choices import HallOfChoices

class Engine(object):

    def __init__(self,scene_map):
        self.scene_map = scene_map


    def play(self):
        current_scene = self.scene_map.opening_scene()

        while True:
            print "\n-------------------"
            next_scene_name = current_scene.enter()
            # current_scene = self.scene_map.next_scene(next_scene_name)


class Map(object):

    scenes = {
        'death':Death(),
        'gold_room':GoldRoom(),
        'panda_room':PandaRoom(),
        'koi_pond_room':KoiPondRoom(),
        'bear_room':BearRoom(),
        'bat_room':BatRoom(),
        'win':Win(),
        'hall_of_choices':HallOfChoices()
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene

    def next_scene(self,scene_name):
        return Map.scenes.get(scene_name)

    def opening_scene(self):
        return self.next_scene(self.start_scene)
