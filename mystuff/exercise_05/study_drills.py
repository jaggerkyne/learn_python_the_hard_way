#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# 1: change all the variables so there isn't the my_ in front.

name = "Jagger Kyne"
age = 33 # this is true
height = 1.68 # in meters
weight = 70.0 # in kgs
eye = "Brown"
teeth = "White"
hair = "black"

print "Let's talk about %s." % name
print "He's %d meter tall." % height # %d makes 1.68 to 1.
print "He's %s meter tall." % height
print "He's %d kg heavy." % weight
print "Actually that's a bit heavy."
print "He's got %s eyes and %s hair." % (eye,hair)
print "His teeth are usually %s depending on the tea." % teeth

# this line is tricky, try to get it exactly right

print "If I add %d, %d, and %d I get %d." % (age,height,weight,age+height+weight)

# %d is for integer and %s is for string

# 2. Try more format characters. %r is useful one. It's like saying "print this no matter what."

will_age = 30

will_tall = 1.73

# this line gives result: This is Wilson's age: 30 and he is 1.73 meter tall.
print "This is Wilson's age: %r and he is %r meter tall." % (will_age,will_tall)


# 3. Search online for all the python format characters.

    # %d - signed integer
    # %i - signed integer
    # more at https://docs.python.org/2/library/stdtypes.html#string-formatting-operations

# 4. convert inches into centimeters and pounds into kilos

my_weight_in_kilos = 70.0 # in kilos

my_height_in_centimeters = 168 # in centimeters

# 1 kilo = 2.20462262 pound

my_weight_in_pound = my_weight_in_kilos * 2.20462262

#1 centimeter = 0.393700787 inches

my_height_in_inches = my_height_in_centimeters * 0.393700787

print "My height is %s centimeters and is around %s inches tall. " % (my_height_in_centimeters, round(my_height_in_inches,2))

print "My weight is %s kilos and is about %s pounds heavy." % (my_weight_in_kilos, round(my_weight_in_pound,3))

# variable need to start with a character.