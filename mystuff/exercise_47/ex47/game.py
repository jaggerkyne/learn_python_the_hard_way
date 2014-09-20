# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


class Room(object):

    def __init__(self,name,description):
        self.name = name
        self.description = description
        self.paths = {} # map

    def go(self,direction):
        return self.paths.get(direction,None)

    def add_paths(self,paths):
        self.paths.update(paths)
