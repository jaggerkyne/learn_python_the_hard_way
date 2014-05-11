#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


the_count = [1,2,3,4,5]
fruits = ['apple','orange','pears','apricots']
change = [1, 'pennies',2,'dimes',3,'quarters']

#This is first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# Also we can go through mixed lists too
# Notice we have to use %r since we don't know what's in it

for i in change:
    print "I got %r" % i

# We can also build lists, first start with an empty one
elements = []

# the use the range function to do 0 to 5 counts

for i in range(0,6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out to

for i in elements:
    print "Element was %d" % i
