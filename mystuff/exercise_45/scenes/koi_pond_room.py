# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from scene import Scene

# TODO make the choice 
class KoiPondRoom(Scene):

    questions = {
        "question_1":"What would you do when you are short of supplies and encounter enemy troop?",
        "question_2":"Where is God?",
        "question_3":"What makes an army invincible?",
        "question_4":"What list below is your favor?",
        "question_5":"At the end of the world, what do you want to save?",
        "question_6":"What do you care most when you take on a troop?",
        "question_7":"What is your dream troop?",
    }

    def enter(self):

        decisions = 0
        print "Welcome to the room of Koi Pond!"
        print "Please answer the following questions carefully."
        print "Your choices will determine your destiny."

        # question 1
        print "What would you do when you are short of supplies and encounter enemy troop?"
        print "1. Retreat"
        print "2. Defense"
        print "3. Offense"

        choice = raw_input(">")

        if int(choice) == 1:
            decisions += 1
        elif int(choice) == 2:
            decisions += 2
        elif int(choice) == 3:
            decisions += 3
        else:
            pass

        # question 2
        print "Where is God?"
        print "1. In my heart."
        print "2. In Heaven."
        print "3. God do not exist."

        choice = raw_input(">")

        if int(choice) == 1:
            decisions += 1
        elif int(choice) == 2:
            decisions += 2
        elif int(choice) == 3:
            decisions += 3
        else:
            pass

        # question 3
        print "What makes an army invincible?"
        print "1. The arm power."
        print "2. The commander."
        print "3. Mobility."

        choice = raw_input(">")

        if int(choice) == 1:
            decisions += 1
        elif int(choice) == 2:
            decisions += 2
        elif int(choice) == 3:
            decisions += 3
        else:
            pass

        # question 4
        print "What list below is your favor?"
        print "1. The aroma of the salty wind."
        print "2. The breeze in the spring."
        print "3. The breeze."

        choice = raw_input(">")

        if int(choice) == 1:
            decisions += 1
        elif int(choice) == 2:
            decisions += 2
        elif int(choice) == 3:
            decisions += 3
        else:
            pass

        # question 5
        print "At the end of the world, what do you want to save?"
        print "1. The people of the world."
        print "2. The knowledge of the world."
        print "3. Myself."

        choice = raw_input(">")

        if int(choice) == 1:
            decisions += 1
        elif int(choice) == 2:
            decisions += 2
        elif int(choice) == 3:
            decisions += 3
        else:
            pass

        # question 6
        print "What do you care most when you take on a troop?"
        print "1. Enough troop."
        print "2. The troops I can control."
        print "3. Hi Morale."

        choice = raw_input(">")

        if int(choice) == 1:
            decisions += 1
        elif int(choice) == 2:
            decisions += 2
        elif int(choice) == 3:
            decisions += 3
        else:
            pass

        # question 7
        print "What is your dream troop?"
        print "1. My strength is important than my troop."
        print "2. High defense power."
        print "3. The absolutely power to crush my enemies."

        choice = raw_input(">")

        if int(choice) == 1:
            decisions += 1
        elif int(choice) == 2:
            decisions += 2
        elif int(choice) == 3:
            decisions += 3
        else:
            pass

        if decisions in range(7,12):
            pass
        elif decisions in range(13,17):
            pass
        elif decisions in range(17,21):
            pass
        else:
            return 'death'

        print "Ok, this is the gifts you receive from me."

        return 'win'