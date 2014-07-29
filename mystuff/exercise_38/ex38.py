# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

# a list of objects separated with ' '
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# print out some strings.
print "Wait there's not 10 things in that list, let's fix that."

# split ten_things by using ' ' and put them into list stuff.
stuff = ten_things.split(' ')

# a list of more stuff
more_stuff = ["Days", "Night", "Song", "Frisbees", "Corn", "Banana","Girl","Boy"]

# checking if the list stuff have 10 items.
while len(stuff) != 10:
    # capture the popped item.
    next_one = more_stuff.pop()
    # print out some strings and the popped item.
    print "Adding: ", next_one
    # append popped item into list stuff
    stuff.append(next_one)
    #print out some strings and the lens of list stuff
    print "There's %d items now. " % len(stuff)

# print out some strings and the list stuff
print "There we go: ", stuff


# print out strings.
print "Let's do some things with stuff."

# print out the item with index number 1
print stuff[1]

# print out the last item in list stuff
print stuff[-1] # whoa! fancy!

# print out the popped item in list stuff
print stuff.pop()

# join all items in list stuff with " "
print " ".join(stuff) # what? cool!

# join items with index 3 and index 4 in list stuff by symbol #
print "#".join(stuff[3:5]) # Super stellar! from position 3 to position 4.

# Study Drills

# 1. Take each function that is called, and go through the steps outlined above to translate them to what
# Python does. For example, ' '.join(things) is join(' ', things).

# 2. Translate these two ways to view the functions calls. For example, ' '.join(things) reads as,
# "Join things with '' between them. " Meanwhile, join(' ', things) means, "Call join with '' and things." Understand
# how they are really the same thing.

# 3. Go read about "object-oriented programming" online. Confused? I was too. Do not worry. You will learn enough to be
# dangerous and you can slowly learn more later.
# Good read: http://www.tutorialspoint.com/python/python_classes_objects.htm

# Example:
# create a pet class

class pet:

    number_of_legs = 0

    def sleep(self): # self must be in (), self means the current object.
        print "zzzZZZ"

    def count_legs(self):
        print "I have %d legs. " % self.number_of_legs

# doug = pet()    # instance of a class pet
#
# doug.number_of_legs = 4 # defined the number of legs are 4.
#
# print "Doug has %d legs." % doug.number_of_legs
#
# doug.sleep()
#
# nemo = pet()
# nemo.number_of_legs = 0
# nemo.count_legs()

# Inheritance

class dog(pet): # dog class inheritance pet class

    def bark(self):
        print "woof!"

dout = dog()
dout.bark()
dout.sleep()
dout.number_of_legs = 4
dout.count_legs()


# 4. Read up on what a "class" is in python. Do not read about how other languages use the word "class". That
#  will only mess you up.

# 5. What's the relationship between dir(something) and the "class" of something?

# 6. If you do not have any idea what I'm talking about, do not worry. Programmers like to feel smart, so they invent
# object-oriented programming, named it OOP, and then used it way too much. If you think that's hard, you should try
# to use "functional programming."