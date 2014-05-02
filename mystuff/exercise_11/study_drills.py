#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# 1. Go online and find out what Python's raw_input does.

# In Python 2.7.6, there are difference between input() and raw_input():
# raw_input() returns a string and input() returns integer or floating number. website: http://www.pythonclub.org/python-basic/input
# input() function will try to convert things you enter as if they were python code, but this is a security hole.

# raw_input(): https://docs.python.org/2/library/functions.html#raw_input
# input(): https://docs.python.org/2/library/functions.html#input

# 2. Can you find other way to use it? Try some of the samples you find.

# 3. Write another "form" like this to ask some other questions.

print "What country are you from?",
citizenship = raw_input()

print "What is your dream?",
dream = raw_input()

print "How many people in your house?",
people = raw_input()

print "So, you are from %s, and you have a dream of %s and you have %s people in your house?" % (citizenship,dream,people)
print "So, you are from %r, and you have a dream of %r and you have %r people in your house?" % (citizenship,dream,people)
# 4. Related to escape sequences, try to find out why the last line has '6\'2"' with that \' sequence.
    # See how the single-quote needs to be escaped because otherwise it would end the string?

# input 6'2" under the usage of %r becoming '6\'2"' because we want to use ' between ''