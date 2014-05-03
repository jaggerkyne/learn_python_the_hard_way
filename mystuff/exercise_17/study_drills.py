#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

# 1. Go read on Python's import statement, and start python to try it out. Try importing some things and see if you can
# get it right. It's alright if you do not.

# 2. This script is really annoying. There's no need to ask you before doing the copy, and it prints too much out to
# the screen. Try to make it more friendly to use by removing features.

# 3. See how short you can make the script. I could make this one line long.

from sys import argv; script, from_file, to_file = argv; open(to_file,'w').write(open(from_file).read())

# the minimum I can write is 3 lines. But does above mean one line.

# 4. Notice at the end of the WYSS I used something call cat? It's just an easy way to print a file to the screen.
# Type man cat to read about it.

# 5. Windows people, find the alternative to cat that Linux/OSX people have.
# Do not worry about man since there is nothing like that.

# 6. Find out why you had to do output.close() in the code.
# The reason we need to close file because Python does not promise will close the file for you.
# In small program, it will be alright, but if in large program, this bad practice may lead to
# running out computer resources and cause error.
