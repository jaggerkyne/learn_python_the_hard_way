#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from sys import argv

script, user_name = argv

print "Hi %s, I'm the %s script." % (user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input()

print "Where do you live %s?" % user_name
lives = raw_input()

print "What kind of computer do you have?"
computer = raw_input()

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice
""" %(likes,lives,computer)

#########
# run in Terminal
# $python ex14.py zed
# Hi zed, I'm the ex14.py script.
# I'd like to ask you a few questions.
# Do you like me zed?
# yes
# Where do you live zed?
# China
# What kind of computer do you have?
# MacAir
#
# Alright, so you said 'yes' about liking me.
# You live in 'China'. Not sure where that is.
# And you have a 'MacAir' computer. Nice