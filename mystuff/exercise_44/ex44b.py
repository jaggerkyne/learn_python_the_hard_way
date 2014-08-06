# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

### Remember: Most of the uses of inheritance can be simplified or replaced
# with composition, and multiple inheritance should be avoided at all costs.

# Parent class is the base class in this example, Child is the subclass.

class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):
    def override(self): # override the parent override()
        print "Child override()"

dad = Parent()
son = Child()

dad.override()
son.override()
