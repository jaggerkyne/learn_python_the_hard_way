# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from sys import exit
from random import randint
from scene import Scene

class Death(Scene):

    death_note = [
        "You are dead now!",
        "You suck at this, my dog is better than this!",
        "Try harder, you just got killed!",
        "Good luck next time!",
        "My goodness, you must be joking, you are dead AGAIN!",
        "How many times you have to die in order to get this game?"
    ]

    def enter(self):
        print Death.death_note[randint(0,len(self.death_note)-1)]
        exit(1)