#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


print "How old are you?", # we put "," at the end of each print line so that print doesn't end the line with a new line
age = raw_input()           # character and go to the next line.
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()
print "So, you're %r year(s) old, %r centimeters tall and %r kilos heavy." % (age,height,weight)
print "So, you're %s year(s) old, %s centimeters tall and %s kilos heavy." % (age,height,weight)
