#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

#1. Convert this while-loop to a function that you can call, and replace 6 in the test(i <6) with a variable.

numbers = []

def print_some_nums():
    i = 0
    counter = 16
    while i < counter:
        print "At the top i is %d" %i
        numbers.append(i)
        i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print_some_nums()

print "Emptying numbers......."
numbers =[]
#2. Now use this function to rewrite the script to try different numbers.

def print_some_nums(counter):
    i = 0
    while i < counter:
        print "At the top i is %d" %i
        numbers.append(i)
        i += 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print_some_nums(20)

print "Emptying numbers........"
numbers =[]

#3. Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8, so
# you can change how much it increments by.

def print_some_nums(counter,step):
    i = 0
    while i < counter:
        print "At the top i is %d" %i
        numbers.append(i)
        i += step
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print_some_nums(20,3)

print "Emptying numbers........"
numbers =[]
#4. Rewrite the script again to use this function to see what effect that has.

#5. Now, write it to use for-loops and range instead. Do you need the incrementor in the middle anymore?
# What happens if you do not get rid of it?

def print_some_nums(counter,step):
    i = 0
    for i in range(0,counter):
        print "At the top i is %d" %i
        numbers.append(i)
        # i += step
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

print_some_nums(20,4)

# if I stop using incrementor, the only change is at the bottom i value. The rest are the same.

# for-loop can only iterate over collections of things.
# while-loop can do any kind of looping you want.
# while-loop is harder to get right, you can get many done with for-loop.

