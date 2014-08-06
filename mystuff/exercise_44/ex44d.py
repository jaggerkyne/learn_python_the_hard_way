# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


class Parent(object):
    
    def override(self):
        print "PARENT override()"
    def implicit(self):
        print "PARENT implicit()"
    def altered(self):
        print "PARENT altered()"

class Child(Parent):
    
    def override(self):
        print "CHILD override()"
    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child,self).altered() # call super with arguments Child and self then call altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.altered()
son.altered()

dad.override()
son.override()

# Method Resolution Order (MRO)