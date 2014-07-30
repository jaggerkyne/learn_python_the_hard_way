# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# Dictionaries, Python calls them dicts, other programming calls them hashes.

# with list, you can only use numbers to get items out of a list.
# dicts allows you use anything as key.

# create a mapping of state to abbreviation
# states = {
#     'Oregon':'OR',
#     'Florida':'FL',
#     'California':'CA',
#     'New York':'NY',
#     'Michigan':'MI'
# }

# create a basic set of states and some cities in them
# cities = {
#     'CA':'San Francisco',
#     'MI':'Detroit',
#     'FL':'Jacksonville'
# }
#
# # add some more cities
# cities['NY'] = 'New York'
# cities['OR'] = 'Portland'
#
# # print out some cities
# print '-' * 10
# print "NY States has: ", cities['NY'] # New York
# print "OR States has: ", cities["OR"] # Portland
#
# # print some states
# print "-" * 10
# print "Michigan's abbreviation is: ", states['Michigan'] # MI
# print "Florida's abbreviation is: ", states['Florida'] # FL
#
# # do it by using the state then cities dict
#
# print "-" * 10
# print "Michigan has: ", cities[states['Michigan']] # Detroit
# print "Florida has: ", cities[states['Florida']] # Jacksonville
#
# # print every state abbreviation
#
# print "-" * 10
# for state,abbrev in states.items():
#     print "%s is abbreviation %s " % (state,abbrev)
#
#
# # print every city in state
# print "-" * 10
# for abbrev, city in cities.items():
#     print "%s has the city %s" % (abbrev,city)
#
# # now do both at the same time
#
# print "-" * 10
# for state, abbrev in states.items():
#     print "%s state is abbreviated %s and has city %s. " % (state,abbrev,cities[abbrev])
#
# print '-' * 10
# # safely get an abbreviation by state that might not be there
# state = states.get('Texas', None)
#
# if not state:
#     print "Sorry, no Texas."
#
# # get a city with a default value
# city = cities.get('TX', "Does Not Exist")
# print "The city for the state 'TX' is: %s " % city
#
# Study Drills

# 1. Do this same kind of mapping with cities and states/regions in
# your country or in some other country.

# please refer to china_cities.py

# 2. Go find the Python documentation for dictionaries (a.k.a. dicts, dict),
# and try to do even more things to them.

# 3. Find out what you can't do with dictionaries. A big limitation is that
# they do not have order, so playing with that.