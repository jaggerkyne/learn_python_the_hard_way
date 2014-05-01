# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


cars = 100 # total number of cars

space_in_a_car = 4.0 # a car can take 4 people
drivers = 30 # total 30 drivers
passengers = 90 # total 90 passengers
cars_not_driven = cars - drivers # cars without drivers
cars_driven = drivers # the number of cars driven is determine by the number of drivers.
carpool_capacity = cars_driven * space_in_a_car # total number of passengers all cars can take
average_passengers_per_car = passengers/cars_driven # the number of passengers place evenly among cars driven

print "There are", cars, "cars available."
print "There are only",drivers,"drivers available."
print "There will be",cars_not_driven,"empty cars today."
print "We can transport",carpool_capacity,"people today."
print "We have",passengers,"to carpool today."
print "We need to put about",average_passengers_per_car,"in each car."