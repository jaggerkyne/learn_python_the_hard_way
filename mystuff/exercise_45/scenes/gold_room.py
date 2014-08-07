# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from scene import Scene

# TODO Gold Room Scene
class GoldRoom(Scene):

    def enter(self):
        print ""

        print "1. Draw a gun and shot!"
        print "2. Give him a joke!"
        print "3. Dodge out of the room now!"


        action = raw_input(">")

        if int(action) == 1:
            return 'gold_room'

        elif int(action) == 2:
            return 'panda_room'

        elif int(action) == 3:
            return 'koi_pond_room'

        else:
            print "WTF?"
            return 'death'