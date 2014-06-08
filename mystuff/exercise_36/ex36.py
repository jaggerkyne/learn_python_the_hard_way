#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


from sys import exit

def dead():
    print "You are dead now! Game Over!"
    exit(0)

def gold_room(gold_on_hand):
    print "This is a room full of gold!"

    print "Welcome to my gold room young man, please take some gold with you."

    print "You may need them later."

    gold =int(raw_input(">"))

    if gold <= 10:
        print "Good, you are not greedy. Keep the gold and get out before I change my mind!"
        gold_on_hand = gold
        print "A big wind blow you away!"
        cthulhu_room(gold_on_hand)
    elif gold > 10 and gold <= 50:
        print "Well done, you knows who you are and your position. "
        print "I will let you pass."
        print "You have " + str(gold) + " of gold."
        gold_on_hand = gold
        bear_room(gold_on_hand)
    else:
        print "You are too greedy, I am sending you to hell."
        dead()


def bear_room(gold_on_hand):
    print "This is the room of bears, please choose which door you want to enter?"
    print "Choose wisely or you might become my lunch."
    print "1. left?"
    print "2. right?"
    choice = int(raw_input("<"))
    if choice == 1:
        print "You now enter the room of sleepy brown bear, what are you going to do?"
        print "1. Pay him 10 pcs of gold to get pass."
        print "2. run for your life!"
        print "3. stay at where you are, do not move."

        print "You have " + str(gold_on_hand) + " of gold."
        action = int(raw_input(">"))
        if action == 1 and gold_on_hand >= 10:
            print "Wise choice, I will let you pass."
            gold_on_hand -=10
            print "You have " + str(gold_on_hand) + " of gold."
            dragon_room(gold_on_hand)
        elif action ==1 and gold_on_hand < 10:
            print "Are you kidding me? You do not have enough money."
            print "You have " + str(gold_on_hand) + " of gold."
            dead()
        elif action == 2:
            print "Coward, do you think you can out run me? Die!"
            dead()
        elif action == 3:
            print "What are you doing? Do you want to be my lunch?"
            dead()
        else:
            print "Smart ass, Die!"
            dead()
    else:
        cthulhu_room(gold_on_hand)

# bear_room()


def cthulhu_room(gold_on_hand):
    print "You are at the room of cthulhu."
    print "A big wind is blowing your way, make a choice quickly before you are dead meat."
    print "1. Curse the cthulhu."
    print "2. Pray Lord's prayer."
    choice = int(raw_input(">"))
    if choice == 1:
        print "You are as good as dead."
        dead()
    elif choice ==2:
        print "Well done, my Child and your prayer has been answered. Come!"
        gods_room(gold_on_hand)
    else:
        print "What are you trying to do?"
        dead()

def dragon_room(gold_on_hand):
    print "Welcome to Dragon's room!"
    print "A blazing Dragon is starring at you!"
    print "Make a choice before it fires you!"
    print "1. Give her a lovely smell and say Hello!"
    print "2. Give her some gold to buy your life."
    print "3. Stone her!"

    action = int(raw_input(">"))
    if action == 1:
        print "What are you doing here? Come to slay me?"
        print "1. Yes, I come to kill you."
        print "2. No, I just walking by."
        action = int(raw_input(">"))
        if action == 1:
            print "Are you joking?! Die!"
            dead()
        elif action == 2:
            print "You lair! Die!"
            dead()
    elif action == 2:
        print "Good choice, how much you want to pay for your life?"
        print "1. Pay her 20 pcs of gold for your life."
        print "2. Pay her 30 pcs of gold for your life!"
        action = int(raw_input(">"))
        if action == 1:
            print "It is too cheap, I rather eat you alive!"
            dead()
        elif action == 2 and gold_on_hand >= 30:
            print "Ok, that sounds fair, I will let you pass!"
            gold_on_hand -= 30
            print "You have " + str(gold_on_hand) + " of gold."
            cthulhu_room(gold_on_hand)
        else:
            print "Stupid choice, you are as good as dead now!"
            dead()
    elif action == 3:
        print "Very brave! I will let you pass"
        gods_room(gold_on_hand)
    else:
        print "Playing smart? You are as good as dead."
        dead()

def gods_room(gold_on_hand):
    print "You enter the room of a living God"
    print "What is your wish my child?"
    print "1. Rule the world."
    print "2. Bless me with wealth that lasts for a life time."
    print "3. Give me wisdom to create wealth out of thin air."

    choice = int(raw_input(">"))
    if choice == 1:
        print "Baster! You are dead!"
        dead()
    elif choice == 2:
        print "Ok, you have overcome so many hurtles to get here, this is your blessings."
        gold_on_hand += 10000000000000
        print "Now you have " + str(gold_on_hand) + " pcs of gold but lack of wisdom, you blow it in 20 years....."
        print "And you die poor!"
    elif choice ==3:
        print "Good choice! I will give you the wisdom you ask plus the blessing of wealth that will last a life time."
        gold_on_hand += 10000000000000
        print "Now you have " + str(gold_on_hand) + " pcs of gold"
        print "And since God gives you the wisdom to use this fortunes, you enjoy full" \
              " of your years on earth and die in peace."
    else:
        print "Do you know that I am God?"
        print "Go home!"


def start():
    # keep track the amount of gold on hand.
    # at the beginning of the game, you have zero pcs of gold
    gold_on_hand = 0

    print "You are in a dark room"
    print "There are two doors in front of you, which door do you want to open?"
    print "1. Open the right door."
    print "2. Open the left door."

    choice = int(raw_input(">"))
    if choice == 1:
        gold_room(gold_on_hand)
    elif choice ==2:
        bear_room(gold_on_hand)
    else:
        print "Want to trick the game? You hit on the wall and die."
        dead()

start()