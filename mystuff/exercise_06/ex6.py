#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


x = "There are %d type of people." % 10

binary = "binary"

do_not = "don't"

y = "Those who know %s and those who %s." % (binary,do_not)

print x
print y

print "I said: %r. " % x # %r gives => I said: 'There are 10 type of people.'.

# use single quote within double quote.
print "I also said: '%s'." % y # '%s' gives => I also said: 'Those who know binary and those who don't.'.

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r" # we use %r for debugging, %r print out raw data, use %s to display to user.

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

print w + e
