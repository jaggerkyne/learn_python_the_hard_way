#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# Make new parts of the game and change what decisions people can make.
# Expand the game out as much as you can before it gets ridiculous.

print "You enter a dark room with two doors. Do you go through door #1 or door #2 or door #3?"

door = raw_input(">")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. Scream at the bear."

    bear = raw_input(">")

    if bear == "1":
        print "The bear eats your face off. Good job!"
    elif bear == "2":
        print "The bear eats your legs off. Good job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear
elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input(">")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good Job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"
elif door == "3":
    print "You stumble around and fall on a knife and die. Good job!"

else:
    print "Cheating, you are knocking into a wall!"