#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# variables in function are not connected to the variables in the script

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"


print "We can just give the function numbers directly:"

# call cheese_and_crackers()
cheese_and_crackers(20,30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# call cheese_and_crackers()
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print "We can even do math inside too:"

# call cheese_and_crackers()
cheese_and_crackers(10+20,5+6)

print "And we can combine the two, variables and math:"

# call cheese_and_crackers()
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers+1000)