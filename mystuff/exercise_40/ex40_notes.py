# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'
import mystuff

#### Dictionaries ####

my_stuff = {'apple':'I AM APPLES!'}

# prints I AM APPLES!
print my_stuff['apple'] # get apple from a dict


##### Modules are like dictionaries ####
### A module is a specialized dictionary that can store Python code
#  so you can access it using "." operator.

# A module is a Python file with some functions or variables in it.
# This file must be imported before you can access it in other Python file.
# You can access a module after importing it using "." operator.

mystuff.apple() # calls the apple() method in mystuff module.

print mystuff.tangerine # access variable tangerine in mystuff module.

#### Classes are like mini-modules ####
### A class is a way to take a grouping of functions and data and place
# them inside a container so you can access them with the '.' operator.

# Classes are like blueprints or definitions for creating new mini-modules.
# Instantiation is how you make one of these mini-modules and import it at the same time.
# The resulting created mini-module is called an object and you then assign it to
# a variable to work with it.

class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now thousand years between"

    def apple(self):
        print "I AM CLASSY APPLES!"

# Why choose class rather than module?
# You can only import a module once, but with class, you can craft with millions of them.

#### Objects Are like Mini-imports. ####

thing = MyStuff() # instantiate an MyStuff object called thing.
thing.apple()
print thing.tangerine