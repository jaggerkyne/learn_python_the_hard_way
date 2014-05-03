#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

#import from sys and os.path.
from sys import argv
from os.path import exists

# set arguments
script, from_file, to_file = argv

# tells the user we are going to copy contents from file A to file B.
print "Copying from %s to %s." % (from_file,to_file)

# we could do these two on one line too, how?
# in_file = open(from_file)
# indata = in_file.read()
# open the from file and read its content to create a file object.
indata = open(from_file).read()

# tell the user about the size of the target file.
print "The input file is %d bytes long." % len(indata)

# check if the destination file exist?
print "Does the output file exist? %r" % exists(to_file) + '.'

# ask if the user want to continue
print "Ready, hit RETURN to continue, CTRL-C or ^C to abort."
raw_input("?")

# open the out_file with write mode.
out_file = open(to_file,'w')

# write data copied from the from_file into out_file
out_file.write(indata)

# give user indication that task is finish.
print "Alright, all done."

# close out_file
out_file.close()

# close in_file
# in_file.close()