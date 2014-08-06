# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# example of using composition

# Three guide line to use composition:

# 1. Avoid multiple inheritance at all costs;
# 2. Use composition to package up code into modules that are used \
# in many different unrelated places and situations.
# 3. Use inheritance only when there are clearly related reusable code that fit under \
# a single common concept or if you have to because of something you're using.

# OOP is just a social convention programmers have created to package and share code.
# The usage of OOP concept differs from group to group, learn how your partners use it in \
# the particular way and adapt to the situation.


class Other(object):


    def override(self):
        print "OTHER override()"


    def implicit(self):
        print "OTHER implicit()"


    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        self.other = Other()


    def implicit(self):
        self.other.implicit()


    def override(self):
        print "CHILD override()"


    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()
son.implicit()
son.override()
son.altered()

#### Study drill: http://legacy.python.org/dev/peps/pep-0008/

# The best way to master the art the problem solving is to solve
# the problem yourself if you got time. Try all the possible solutions and practice makes perfect.

# In Python, classes are templates that "mint" new objects, similar to
# how coins were minted using a die (template).

# Naming Convention:

# Class names should normally the CapWords convention.

# Exception is class and with Error_ prefix.

# Global variables names

# Function Names should be lowercase, with words separated by underscores to improve readability.

# Function and method arguments:
# 1. Always use self for the first argument to instance methods.
# 2. Always use cls for the first argument to class method, if naming clashes, use synonym.

# Method Names and instance Variables.
# 1. Use function naming rules: lowercase with words separated by underscores
# 2. Use one leading underscore only for non-public methods and instance variables.
# 3. use non-public if in doubt, keep things "private" to local classes as possible.

# Pythonic Guidelines:
# 1. Public attributes should have no leading underscores.
# 2. If your public attribute name collides with a reserved keyword, append a single \
#  trailing underscore to your attribute name.
# 3. For simple public data attributes, it is best to expose just the attribute name, \
# without complicated accessor/mutator methods.
# 4. If your class is intended to be subclassed, and you have attributes that you do not want \
# subclasses to use, consider naming them with double leading underscores and no trailing underscores.

# Public and internal interfaces
# Documented interfaces are considered public.
# Undocumented interfaces should be assumed to be internal.
# modules should explicitly declare the names in their public API using the __all__ attributes.
# setting __all__ to an empty list indicates that the module has no public API.
# Even with __all__ set appropriately, internal interfaces (packages, modules, classes, functions \
# attributes or other names) should still be prefixed with a single leading underscore.
#An interface is also consider internal if any containing namespace (package, modules or class) \
#  is considered internal.
