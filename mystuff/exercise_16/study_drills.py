#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# 1. If you feel you do not understand this, go back through and use the comment trick to get it squared away in your
# mind. One simple English comment above each line will help you understand or at least let you know what you need to
# research more.


# import argv from sys package.
from sys import argv

# variables needed to use the script in command line
script, filename = argv

# tell the user what is about to do.
print "We're going to erase %r. " % filename
print "If you don't want that, hit CTRL-C if you are in windows and ^C if you are in Mac."
print "If you do want that to happen, hit RETURN."

# waiting for user's input.
raw_input("?")

# tell the user the script is opening the target file.
print "Opening the file...."
# open the file with the purpose to write into a file
target = open(filename,'w')

# tell the user the script is about to truncating the file.
print "Truncating the file. Goodbye!"

# truncating the file.
target.truncate()

# gives instruction what the script is about to do.
print "Now I'm going to ask you for three lines."

# get inputs from the user
line1 = raw_input("Line 1:")
line2 = raw_input("Line 2:")
line3 = raw_input("Line 3:")

# tell the user what the script is about to do.
print "I'm going to write these to the file."

# write lines into file
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')



# print out instruction
print "Finally, we are closing the file."

# close the file
target.close()

# 2. Writes a script similar to the last exercise that uses read and argv to read the file you just create.

txt = open(filename,'r')
content =txt.read()
print "This is the content inside of %r " % txt + content

# 3. There's too much repetition in this file. Use strings, formats and escape to print out line1, line2 and line3
# with just one target.write() command instead of six.
#
# user_input = line1 + '\n' + line2 + '\n' + line3 + '\n'
# target.write(user_input)

# 4. Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by making you explicitly
# say you want to write a file.

# 'w' tell the purpose of opening the file.

# 5. If you open the file with 'w' mode, then do you really need the target.truncate()?
# Go read the docs for Python's open function and see if that's true.

# when you enter 'w' mode, it will override the file anyway, use target.truncate() is redundant.
