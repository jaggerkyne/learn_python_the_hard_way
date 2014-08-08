# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from scene import Scene

# Gold Room
class GoldRoom(Scene):

    def enter(self):
        print "After open the door at Gold Room, you saw a room full of gold."
        print "There is no light in the room, but somehow the room is glowing with golden lights."
        print "You see a lot of gold pieces laid on the ground."
        print "What is your choice?"

        print "1. run into the room and begin to pick up some gold!"
        print "2. be cautious and slowly move towards the gold."
        print "3. turn back and walk away."


        action_0 = raw_input(">")

        if int(action_0) == 1:
            print "You run towards the gold and hear a sound of 'Click','Click'."
            print "An array of gold bar drop from the sky block your way to the gold."
            print "What to do now?"
            print "1. take a knife and start chopping the gold bar."
            print "2. cruse at the the gold bars. "
            print "3. turn around and run."

            action_1 = raw_input(">")

            if int(action_1) == 1:
                print "Hahaha! What are you doing? A knife to cut the gold bar?"
                print "Your attitude is interesting, I will let you live."
                return 'koi_pond_room'

            elif int(action_1) == 2:
                print "WTF? You are rude, go to die!"
                return 'death'

            elif int(action_1) == 3:
                print "You are luck as you turn around, the wall above your head begin to press down."
                return 'hall_of_choices'
            else:
                print "WTF? You choice is no on the list."
                return 'death'

        elif int(action_0) == 2:
            return 'panda_room'

        elif int(action_0) == 3:
            return 'hall_of_choices'

        else:
            print "WTF?"
            return 'death'