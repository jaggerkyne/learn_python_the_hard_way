#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


formatter = "%r %r %r %r"

print formatter % (1,2,3,4)

print formatter % ("one","two","three","four")

print formatter % (True,False,False,True)

print formatter % (formatter,formatter,formatter,formatter)

print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)