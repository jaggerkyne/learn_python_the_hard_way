#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

# 1 Go through this program and write comment above each line explaning it.

# put variable x to store  string and put a format specifier within a string
x = "There are %d type of people." % 10

# variable binary stores string "binary"
binary = "binary"

# variable do_not stores string "don't"
do_not = "don't"

# put the variables into an existing string.
y = "Those who know %s and those who %s." % (binary,do_not)

# print result of x
print x

# print result of y
print y

# put variable x into an existing string
print "I said: %r. " % x # %r gives => I said: 'There are 10 type of people.'.

# put variable y into an existing string
print "I also said: '%s'." % y # '%s' gives => I also said: 'Those who know binary and those who don't.'.

# assigned a value False into variable hilarious
hilarious = False

# assigned a string values into variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# print result of two variables.
print joke_evaluation % hilarious

# assigned strings into variable w
w = "This is the left side of..."

# assigned string into variable e
e = "a string with a right side."

# print w
print w + e

# 2 Find all the places where a string is put inside a string.

# 2.1 -> y = "Those who know %s and those who %s." % (binary,do_not)
# 2.2 -> print "I said: %r. " % x
# 2.3 -> print "I also said: '%s'." % y
# 2.4 -> print joke_evaluation % hilarious

# 3 Are you sure there are only four places? How do you know? Maybe I like lying.

# Well, x = "There are %d type of people." % 10 looks like, but 10 is integer, not a string so it is not a string is put
# into a string.

# If this is true, 2.4 can be argued is not true as well,
# because False technically is not a string, but an evaluation value.

# 4 Explain why adding the two strings w and e with + makes a longer string.
# using plus sign (+) between two strings connect them together.

