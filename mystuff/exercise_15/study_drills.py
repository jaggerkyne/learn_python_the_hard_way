#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


#1. Above each line, write out in English what that line does.

# # import argv from sys
# from sys import argv
#
# # set variables in batch
# script, filename = argv
#
# # # open a file and create a 'file object' and assign to variable txt, it does not return the contents of the file
# txt = open(filename)
#
# # print out the name of the file
#
# print "Here's your file %r: " % filename
#
# # print the content of the file
# print txt.read()
#
# # ask the user to type the file name again
# print "Type the filename again:"
#
# # print out the prompt symbol to wait for user input
# file_again = raw_input(">")
#
# # open the file again and store it in txt_again
# txt_again = open(file_again)
#
# # print out the content of the txt_again.
# print txt_again.read()

#2. If you are not sure, ask someone for help or search online. Many times searching for "Python THINGS" will
# answers for what that THING does in Python. Try searching for "python open".

# https://docs.python.org/2/library/functions.html#open
# open(name[, mode[, buffering]])

# name is the file name want to open.
# mode is optional default is r, value could be w, r, a (which stands for write, read and append)

#3. I used the name "commands" here,
# but they are also called "functions" and "methods". Search around online
# to see what other people do to define these. Do not worry if they confuse you. It's normal for programmers to
# confuse you with vast extensive knowledge.

# methods and functions commands are the same thing, they are ways to perform something useful.

#4. Get rid of part from lines 10 - 15 where you use raw_input and try the script then.

# from sys import argv
#
# # set variables in batch
# script, filename = argv
#
# # # open a file and create a 'file object' and assign to variable txt, it does not return the contents of the file
# txt = open(filename)
#
# # print out the name of the file
#
# print "Here's your file %r: " % filename
#
# # print the content of the file
# print txt.read()

# in the Terminal it shows:
#
# $python study_drills.py ex15_sample.txt
# Here's your file 'ex15_sample.txt':
# This is stuff I typed into a file.
# It is really cool stuff.
# Lots and lots of fun to have in here.

#5. Use only raw_input and try the script that way. Think of why one way of getting the filename would be
# better than another.
# argv is better than user input, user input relies on people and people make mistakes.

#6. Run pydoc file and scroll down until you see the read() command (method/function).
# See all the other ones you can use? Skip the ones that have __(two underscores) in front because those are junk.
# Try some of the other commands.
# two examples of methods:

# file.read()
#
# file.close()
#

# # import argv from sys
# from sys import argv
#
# # set variables in batch
# script, filename = argv
#
# # # open a file and create a 'file object' and assign to variable txt, it does not return the contents of the file
# txt = open(filename)
#
# # print out the name of the file
#
# print "Here's your file %r: " % filename
#
# # read the first line in the file.
# print txt.readline()


#7. Star python again and use open from the prompt. Notice how you can open files and run read on them right there?

# in the Terminal, you can use open ex15_sample.txt to open this file and use 'more' or 'less' to read the file right there.

# When I got into python mode, txt = open(ex15_sample.txt) throw NameError: name 'ex15_sample' is not defined.
# this is in python, I need to specify the path for the file, when I use below code, it works:
#
# f = open('/Users/Jagerkyne/Documents/Sites/python/learn_python_the_hard_way/mystuff/exercise_15/ex15_sample.txt')
#
# >>> f.read()
# 'This is stuff I typed into a file.\nIt is really cool stuff.\nLots and lots of fun to have in here.'

#8. Have your script also do a close() on the txt and txt_again variables. It's important to close files when
# you are done with them.


# # import argv from sys
# from sys import argv
#
# # set variables in batch
# script, filename = argv
#
# # # open a file and create a 'file object' and assign to variable txt, it does not return the contents of the file
# txt = open(filename)
#
# # print out the name of the file
#
# print "Here's your file %r: " % filename
#
# # read the first line in the file.
# print txt.readline()
#
# txt.close()

# Python will not restrict I from opening a file more than once, sometime it is necessary
#  but it is good practice that we need to close a file when we done with it.