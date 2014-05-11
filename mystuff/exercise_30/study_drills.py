#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


#1. Try to guess what elif and else are doing.

# if condition is true, execute this block of code, elif stands for else-if, if the first block of code is not true,
# execute the second block of code. else, if the first 2 blocks of code are false,
# then execute whatever code behind "else:".

#2. Change the numbers of cars, people, and buses, and then trace through each if-statement to see what will printed.
#3. Try some more complex boolean expressions like cars > people and buses < cars.
people = 40
cars = 40
buses = 15
    # if condition
if cars > people:
    # print out result.
    print "We should take the cars."
elif cars < people: #elif block
    # print out result.
    print "We should not take the cars."
else: # else block
    # print out result.
    print "We can't decide."

    # if statement.
if buses > cars:
    # print out result.
    print "That's too many buses."
    # elif block
elif buses < cars:
    # print out result.
    print "Maybe we could take the buses."
else: # else block
    # print out result.
    print "We still can't decide."

if people > buses:
    # print out result.
    print "Alright, let's just take the buses."
else:# else block
    # print out result.
    print "Fine, let's stay home then."

#4. Above each line, write an English description of what the line does.
#
# people = 30
# cars = 40
# buses = 15
#     # if condition
# if cars > people:
#     # print out result.
#     print "We should take the cars."
# elif cars < people: #elif block
#     # print out result.
#     print "We should not take the cars."
# else: # else block
#     # print out result.
#     print "We can't decide."
#
#     # if statement.
# if buses > cars:
#     # print out result.
#     print "That's too many buses."
#     # elif block
# elif buses < cars:
#     # print out result.
#     print "Maybe we could take the buses."
# else: # else block
#     # print out result.
#     print "We still can't decide."
#
# if people > buses:
#     # print out result.
#     print "Alright, let's just take the buses."
# else:# else block
#     # print out result.
#     print "Fine, let's stay home then."