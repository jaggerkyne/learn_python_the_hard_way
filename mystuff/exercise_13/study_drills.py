#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# 1. Try giving few than three arguments to your script. See that error you get? See if you can explain it.

# run ex13.py in Terminal with following command
# python ex13.py first 2nd

# gives the below error message:
#
# Traceback (most recent call last):
#   File "ex13.py", line 10, in <module>
#     script, first, second, third = argv # argv is argument variable
# ValueError: need more than 3 values to unpack

# This means we need at least 3 values to allow this script to unpack
# I also try to give 4 value like below
# python ex13.py first 2nd 3rd 4th
# gives the below error message:

# $python ex13.py first 2nd 3rd 4th
# Traceback (most recent call last):
#   File "ex13.py", line 10, in <module>
#     script, first, second, third = argv # argv is argument variable
# ValueError: too many values to unpack

# 2. Write a script that has fewer arguments and one that has more. Make sure you give the unpacked variables good names.

####fewer arguments, 2 arguments ###

# from sys import argv
#
# script, first_person, second_person = argv # even we only have 2 people to be entered, we need to put script into argv
#
# print "The first person is: ", first_person
# print "The second person is: ", second_person

####fewer arguments, 4 arguments ###

# from sys import argv
#
# script, first_person, second_person, third_person, fourth_person = argv
#
# print "The first person is: ", first_person
# print "The second person is: ", second_person
# print "The 3rd person is: ",third_person
# print "The forth person is:", fourth_person

# 3. Combine raw_input with argv to make a script that gets more input from a user.

from sys import argv

# if you want to give your script inputs on the command line, use argv
script, first_name, last_name, height, weight = argv

# you raw_input() if you want to input using the keyboard while the script is running.
first_name = raw_input("What is your first name?")
last_name = raw_input("What is your last name?")
# raw_input("How tall are you?"), height
# raw_input("How heavy are you?"), weight

print "Hello, my name is %s %s and I am %s tall and %s heavy." % (first_name,last_name,height,weight)

#
# $python study_drills.py wilson jackson angle sophia
# What is your first name?Dog
# What is your last name?Man
# Hello, my name is Dog Man and I am angle tall and sophia heavy.

# 4. Remember that modules give you features. Modules. Modules. Remember this because we'll need it later.

# all command arguments and raw_input come into python as string, you need to convert them as needed.
