# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from scene import Scene
from random import randint

class BearRoom(Scene):

    my_choices = {
        1:"run for your life",
        2:"play dead",
        3:"tell a joke"
    }

    def enter(self):

        print "You are kicked to here, you see a black bear is crawling towards you."

        print "Your life is on your hands."

        print "What do you want to do?"

        print "1. Roll a dice."
        print "2. Throw a rock."
        print "3. Sing a song."
        action = int(raw_input(">"))

        if action == 1:
            random_action = BearRoom.my_choices.get(randint(1,len(BearRoom.my_choices)))
            if random_action == "run for your life":
                print "You jump up and run for your life."
                print "But the bear come close you easily and out run you."
                print "You can see its ugly face but you can't out run it. "
                print "It jumps on you and this is your last sight you see."
                return "death"
            elif random_action == "play dead":
                print "The bear come close to you and smell you face."
                print "What! It licks my face."
                print "You continue to play dead, and this bear bites your head off."
                return "death"
            elif random_action == "tell a joke":
                print "Little bear, let me tell your a joke in bear's tongue."
                print "*&^&(*^(%$&(*#(*()*$&^"
                print "*)(^%&^()*$%$*&(*&*(&*#$$%^$%"
                print "The bear stops, and shout back '*&*(^%(*&(*&&^%*(&(' "
                print "You continue to tell the bear joke."
                print "*(&^&^&^^%^&%&^*&^*&"
                print "For some reason, the bear is speeding up towards you and bites your head off."
                print "WTF, I can speak in human tongue, this guy swear at me using bear's tongue."
                return "death"
            else:
                print "What a fool, you are dead now!"
                return "death"
        elif action == 2:
            print "The rock is on the bear and the bear runs towards you and bite your head off."
            return "death"
        elif action == 3:
            print "You give your best voice to sing a song."
            print "$##@#$$#$$#$#$#$........."
            print "You reminds my mother, I will let you pass, the bear say."
            return "gold_room"
        else:
            print "WTF, you are as good as dead now."
            return "death"


