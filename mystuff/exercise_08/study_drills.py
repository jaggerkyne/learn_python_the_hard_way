#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


formatter = "%r %r %r %r"
formatter_2 = "%s %s %s %s"

print formatter % (1,2,3,4)

print formatter % ("one","two","three","four")

print formatter % (True,False,False,True)

print formatter % (formatter,formatter,formatter,formatter)

print formatter % ("开心","好人","坏人","哈哈哈") # %r gives debugging value.
print formatter_2 % ("开心","好人","坏人","哈哈哈")
# print out 'I had this thing.' 'That you could type up right.' "But it didn't sing." 'So I said goodnight.'
# it comes with both single and double quotes to tell me they are both alright.
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# I should use %s rather than %r in normal situation, only use %r when debugging

#