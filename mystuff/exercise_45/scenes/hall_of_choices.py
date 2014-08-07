# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from scene import Scene

class HallOfChoices(Scene):

    def enter(self):
        print "You are one of the best bounty hunter in the world. One day, you found an old map"
        print "from a bad guy in a run-down whorehouse."
        print "The man asked you to give him a peaceful death as he knew your reputation among the villains."
        print "He gave you this map and you gave him a bullet straight in his head."
        print "After reading the map, you discovered you have seen this map before. "
        print "The map was stolen from your grandpa's house when you last saw your grandpa."
        print "You once promised your grandpa that you will solve the puzzle and get the gold home."
        print "So here you are, you stood in front of hall of trees. In the hall, you see Five giant doors."
        print "The first room labeled 'Gold Room'."
        print "The second room labeled 'Panda Room'."
        print "The third room labeled 'Koi Pond Room'."
        print "The fourth room labeled 'Bear Room'."
        print "The fifth room labeled 'Bat Room'."
        print "Welcome to the room of choice, please decide which room you want to enter?"
        print "The choice will determine your destiny!"
        print "Which room do you choose?"
        print "1. Enter the Gold Room"
        print "2. Enter the Panda Room"
        print "3. Enter the Koi Pond Room"
        print "4. Enter the Bear Room"
        print "5. Enter the Bat Room"

        action = raw_input(">")

        if int(action) == 1:
            return 'gold_room'

        elif int(action) == 2:
            return 'panda_room'

        elif int(action) == 3:
            return 'koi_pond_room'

        elif int(action) == 4:
            return 'bear_room'

        elif int(action) == 5:
            return 'bat_room'

        else:
            print "WTF?"
            return 'death'