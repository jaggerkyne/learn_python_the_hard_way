#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# remember the true false table

#   NOT           TRUE?
# Not false        True
# Not True         Flase


#       OR             True?
# True or False        True
# True or True         True
# False or True        True
# False or False       False

#       AND             True?
# True and False        False
# True and True         True
# False and True        False
# False and False       False


# Not OR                True?
# Not(True or False)    False
# Not(True or True)     False
# Not(False or True)    False
# Not(False or False)   True

# Not And               True?
# Not(True and False)   True
# Not(True and True)    False
# Not(False and True)   True
# Not(False and False)  True

#       !=              True?
#       1 != 0          True
#       1 != 1          False
#       0 != 1          True
#       0 != 0          False

#       ==              True?
#       1 == 0          False
#       1 == 1          True
#       0 == 1          False
#       0 == 0          True