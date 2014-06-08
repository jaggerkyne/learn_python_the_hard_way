#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


#1. Draw a map of the game and how you flow through it.

#2. Fix all your mistakes, including spelling mistakes.

#3. Write comments for the functions you do not understand. Remember doc comments?

#4. Add more to the game. What can you do to both simplify and expand it?

#5. The gold_room has a weird way of getting you to type number. What are all the bugs in this way of doing it?
# Can you make it better than just checking if "1" or "0" are in the number? Look at how int() works for clues.

# simple FizzBuzz game

def fizzBuzz():

    for x in range(0,1000):
        if x % 3 == 0:
            print "Fizz"
        elif x % 5 == 0:
            print "Buzz"
        elif (x % 3 == 0) and (x % 5 == 0):
            print "FizzBuzz............"
        else:
            print x

fizzBuzz()