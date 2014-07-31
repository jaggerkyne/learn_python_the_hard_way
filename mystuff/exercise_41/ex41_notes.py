# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


###### Word Drills #####

# class - tell Python to make a new kind of thing.

# object - Two meanings: the most basic kind of thing, and any instance of some thing.

# instance - What you get when you tell Python to create a class.

# def - How you define a function inside a class

# self - inside the functions in a class, self is a variable for the instance/object being accessed.

# inheritance - The concept that one class can inherit traits from another class,
# much like you and your parents.

# composition - The concept that a class can be composed of other classes as parts,
# much like how a car has wheels.

# attribute - A property classes have that are from composition and are usually variables.

# is-a - A phrase to say that something inherits from another, as in a "salmon" is-a "fish".

# has-a - A phrase to say that something is composed of other things or has a trait, as in
# "a salmon has-a mouth".

###### Phrase Drills #####

# class X(Y)  ---> Make a class named X is-a class Y.

# class X(object):
#   def __init__(self,J):
    # ----> make a class named X is-a class object which
    # has-a __init__ that takes self and J parameters.

# class X(object):
#   def M(self,J):
    # ----> make a class named X is-a class object which
    # has-a function M that takes self and J parameters.

# foo = X() -----> set foo to an instance of class X.

# foo.M(J) ------> from foo to get the M function, call it with parameter J.

# foo.K = Q ------> from foo to get attribute K and set it to Q.

