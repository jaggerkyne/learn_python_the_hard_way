# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from scene import Scene
from koi_pond_room import KoiPondRoom

#
class PandaRoom(Scene):

    gifts_from_panda = {
        "1":"Arrows of Tongue",
        "2":"Snake Oil",
        "3":"Money Masters"
    }
    my_gears = KoiPondRoom.my_gears

    def enter(self):
        print "Welcome to the room of Panda!"
        print "I am the Panda you know."
        print "Yes, I am the dragon worrier."
        print "So, show me what you got from the Koi Pond."


        if PandaRoom.my_gears.pop() == "Shield of Faith":
            print "OK, you got the Shield, let me give you some arrows so you can fight the beast!"
            PandaRoom.my_gears.append(PandaRoom.gifts_from_panda.get("1"))
            return "bear_room"
        elif PandaRoom.my_gears.pop() == "sword of the Spirit":
            print "You got the sword, let me give you some oil to oil it up."
            PandaRoom.my_gears.append(PandaRoom.gifts_from_panda.get("2"))
            return "bat_room"
        elif PandaRoom.my_gears.pop() == "wallet":
            print "What?! You got the wallet, let me give you some money so you can add it up."
            PandaRoom.my_gears.append(PandaRoom.gifts_from_panda.get("3"))
            return "gold_room"
        else:
            print "Sorry, I don't know how you get here, I have to kill you!"
            return 'death'

