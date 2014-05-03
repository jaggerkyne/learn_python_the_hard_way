#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# 1. Go through and write English comments for each line to understand what's going on.

# import argv from sys package.
from sys import argv
# set arguments for command line
script, input_file =argv

def print_all(f):
    #print out the content of the file.
    print f.read()

# rewinding the pointer.
def rewind(f):
    # call seek() function
    f.seek(0)

# take two arguments, one is line counter, second one is the file to be read.
def print_a_line(line_count,f):
    #print out line count and the content of the line.
    print line_count, f.readline()

# read the input_file and create a file object
current_file = open(input_file)

print "First let's print the whole file: \n"

# call print_all() function
print_all(current_file)

print "Now let's rewind, kind of like a tape."

# call rewind() function
rewind(current_file)

print "let's print three lines:"

# # set a pointer
# current_line = 1
#
# # call print_a_line() function
# print_a_line(current_line,current_file) # current_line == 1
#
# # update current_line pointer
# current_line = current_line + 1 # current_line == 2
#
# # call print_a_line() function
# print_a_line(current_line,current_file)
#
# # update the current_line pointer# current_line ==3
# current_line = current_line + 1
#
# # call print_a_line() function
# print_a_line(current_line,current_file)

# 2. Each time print_a_line is run, you are passing in a variable current_line. Write out what current_line is equal
# to on each function call, and trace how it becomes line_count in print_a_line.

# 3. Find each place a function is used, and go check its def to make sure that you are giving the right arguments.

# 4. Research online what the seek function for file does. Try pydoc file and see if you can figure it out from there.
#
# seek(...)
#  |      seek(offset[, whence]) -> None.  Move to new file position.
#  |
#  |      Argument offset is a byte count.  Optional argument whence defaults to
#  |      0 (offset from start of file, offset should be >= 0); other values are 1
#  |      (move relative to current position, positive or negative), and 2 (move
#  |      relative to end of file, usually negative, although many platforms allow
#  |      seeking beyond the end of a file).  If the file is opened in text mode,
#  |      only offsets returned by tell() are legal.  Use of other offsets causes
#  |      undefined behavior.
#  |      Note that not all file objects are seekable.

# 5. Research the shorthand notation += and rewrite the script to use that.

# set a pointer
current_line = 1

# call print_a_line() function
print_a_line(current_line,current_file) # current_line == 1

# update current_line pointer
current_line += + 1 # current_line == 2

# call print_a_line() function
print_a_line(current_line,current_file)

# update the current_line pointer# current_line ==3
current_line +=  + 1

# call print_a_line() function
print_a_line(current_line,current_file)
