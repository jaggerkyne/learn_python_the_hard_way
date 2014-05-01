# Another code written by Jagger Kyne
# Copyright 2006 - 2013 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


my_name = "Jagger Kyne"
my_age = 33 # this is true
my_height = 1.68 # in meters
my_weight = 70.0 # in kgs
my_eye = "Brown"
my_teech = "White"
my_hair = "black"

print "Let's talk about %s." % my_name
print "He's %d meter tall." % my_height # %d makes 1.68 to 1.
print "He's %s meter tall." % my_height
print "He's %d kg heavy." % my_weight
print "Actually that's a bit heavy."
print "He's got %s eyes and %s hair." % (my_eye,my_hair)
print "His teeth are usually %s depending on the tea." % my_teech

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (my_age,my_height,my_weight,my_age+my_height+my_weight)

# %d is for integer and %s is for string
