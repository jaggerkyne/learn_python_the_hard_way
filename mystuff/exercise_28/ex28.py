#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

"""
Process to solve boolean logic statements:
1. Find an equality test (== or !=) and replace it with its truth
2. Find each and/or inside parentheses and solve those first.
3. Find each not and invert it.
4. Find any remaining and/or and solve it.
5. When you are done, you should have True or False.
"""

# Boolean  logic expression

print True and True # True

print False and True # False

print 1 == 1 and 2 == 1 # False

print "test" == "test" # True

print 1 == 1 or 2 != 1 # True

print True and 1 == 1 # True

print "test" == "testing" # False

print 1 != 0 and 2 == 1 # False

print "test" != "testing" # True

print "test" == 1 # False

print not (True and False) # True

print not (1 == 1 and 0 != 1) # False

print not (10 == 1 or 1000 == 1000) # False

print not (1 != 10 or 3 == 4) # False

print not ("testing" == "testing" and "Zed" == "Cool Guy") # True

print 1 == 1 and not ("testing" == 1 or 1 == 0) # True

print "chunky" == "bacon" and not (3 == 4 or 3 == 3) # False

print 3 == 3 and not ("testing" == "testing" or "Python" == "Fun") # False
