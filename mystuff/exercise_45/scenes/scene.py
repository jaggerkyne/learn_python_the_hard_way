# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

class Scene(object):
    # store the number of visit a play visits the scene.
    visit_counter = 0

    def enter(self):
        print "The scene is not yet configured. Subclass it and implement enter()"

