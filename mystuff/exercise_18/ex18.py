#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# this one is like your scripts with argv

# *args is similar like argv
def print_two(*args):
    arg1,arg2 = args
    print "arg1: %r, arg2: %r" % (arg1,arg2)

# ok, that *args is actually pointless, we can just do this
def print_two_again(arg1,arg2):
    print "arg1: %r, arg2: %r" % (arg1,arg2)

# this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

# this one take no arguments

def print_none():
    print "I got nothing."

print_two("Jagger","Kyne")
print_two_again("Jagger",'Kyne')
print_one("First")
print_none()