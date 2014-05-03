#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

# import argv from sys
from sys import argv

# set variables in batch
script, filename = argv

# open a file and create a 'file object' and assign to variable txt, it does not return the contents of the file
txt = open(filename)

# print out the name of the file

print "Here's your file %r: " % filename

# print the content of the file
print txt.read()

# ask the user to type the file name again
print "Type the filename again:"

# print out the prompt symbol to wait for user input
file_again = raw_input(">")

# open the file again and store it in txt_again
txt_again = open(file_again)

# print out the content of the txt_again.
print txt_again.read()