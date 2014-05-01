#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# 1 Go back through and write a comment on what each line does.

# 2 Read each one backward or out loud to find your errors.

# 3 From now on, when you make mistakes, write down on a piece of paper what kind of mistake you make

# 4 When you go to the next exercise, look at the last mistake you make and try not to make them in this new one.

# 5 Remember that everyone makes mistakes. Programmers are like magicians who like everyone to think they are
# perfect and never wrong, but it's all an act. They make mistakes all the time.


# print out string "Mary had a little lamb."
print "Mary had a little lamb."

# put string 'snow' into a long string.
print "Its fleece was white as %s." % 'snow'

# print string
print "And everywhere that Mary went."

# print ten "." (without "")
print "." * 10 # what'd that do? print out ten "." (without "")

# assigned values
end1 = "C"
end2 = 'h'
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# connect 5 variables and print them out
print end1 + end2 + end3 + end4 + end5 + end6, # Cheese
print end7 + end8 + end9 + end10 + end11 + end12 # Burger


# when removed "," (without ""), Cheese Burger will be in separate line.
print end1 + end2 + end3 + end4 + end5 + end6 # Cheese
print end7 + end8 + end9 + end10 + end11 + end12 # Burger

# common questions:

# There are not much differences between single and double quotes in Python. '' is normally for short string.
# Use "," to connect two print together is a bad style.