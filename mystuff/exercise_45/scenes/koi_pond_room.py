# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from scene import Scene

#
class KoiPondRoom(Scene):

    #counter for decision values.
    decisions = 0

    # questions God will ask.
    questions = {
        "question_1":"What would you do when you are short of supplies and encounter enemy troop?",
        "question_2":"Where is God?",
        "question_3":"What makes an army invincible?",
        "question_4":"What list below is your favor?",
        "question_5":"At the end of the world, what do you want to save?",
        "question_6":"What do you care most when you take on a troop?",
        "question_7":"What is your dream troop?",
    }

    # gifts God will give to the player.
    gifts = {
        "1":"Shield of Faith",
        "2":"sword of the Spirit",
        "3":"wallet",
    }

    # player's gear bag
    my_gears = []

    # counting points user earn.
    def choice_counter(self,choice):

        self.choice = int(choice)
        if self.choice == 1:
            KoiPondRoom.decisions += 1
        elif self.choice == 2:
            KoiPondRoom.decisions += 2
        elif self.choice == 3:
            KoiPondRoom.decisions += 3
        else:
            print "Your choice does not exist, please make a choice again!"
            self.choice = raw_input(">")
            self.choice_counter(self.choice)


    # user input
    def user_choice(self):
        choice = raw_input(">")
        self.choice_counter(choice)
        print "decisions is now at %d." % KoiPondRoom.decisions

    def enter(self):

        print "Welcome to the room of Koi Pond!"
        print "Please answer the following questions carefully."
        print "Your choices will determine your destiny."

        # question 1
        print KoiPondRoom.questions.get('question_1')
        print "1. Retreat"
        print "2. Defense"
        print "3. Offense"
        self.user_choice()

        # question 2
        print KoiPondRoom.questions.get('question_2')
        print "1. In my heart."
        print "2. In Heaven."
        print "3. God do not exist."
        self.user_choice()


        # question 3
        print KoiPondRoom.questions.get('question_3')
        print "1. The arm power."
        print "2. The commander."
        print "3. Mobility."
        self.user_choice()


        # question 4
        print KoiPondRoom.questions.get('question_4')
        print "1. The aroma of the salty wind."
        print "2. The breeze in the spring."
        print "3. The breeze."
        self.user_choice()


        # question 5
        print KoiPondRoom.questions.get('question_5')
        print "1. The people of the world."
        print "2. The knowledge of the world."
        print "3. Myself."
        self.user_choice()


        # question 6
        print KoiPondRoom.questions.get('question_6')
        print "1. Enough troop."
        print "2. The troops I can control."
        print "3. Hi Morale."
        self.user_choice()


        # question 7
        print KoiPondRoom.questions.get('question_7')
        print "1. My strength is important than my troop."
        print "2. High defense power."
        print "3. The absolutely power to crush my enemies."
        self.user_choice()


        print "Ok, this is the gifts you receive from me."

        if KoiPondRoom.decisions in range(7,13):
            print "This is your Shield of Faith."

            KoiPondRoom.my_gears.append(KoiPondRoom.gifts.get("1"))

        elif KoiPondRoom.decisions in range(13,17):
            print "This is your sword of the Spirit."
            KoiPondRoom.my_gears.append(KoiPondRoom.gifts.get("2"))
        elif KoiPondRoom.decisions in range(17,22):
            print "This is your wallet."
            KoiPondRoom.my_gears.append(KoiPondRoom.gifts.get("3"))
        else:
            print "I don't know, for some reason, I don\'t like you. Go to Hell."
            return 'death'

        print "My gear has: %s." % KoiPondRoom.my_gears

        print "Now, you can move to the next room, good luck."

        return 'panda_room'