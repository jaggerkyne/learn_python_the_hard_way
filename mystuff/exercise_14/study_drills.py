#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

#1. Find out what Zork and Adventure where. Try to find a copy and play it.

# http://www.web-adventures.org/cgi-bin/webfrotz?s=ZorkDungeon

#2. Change the prompt variable to something else entirely.

from sys import argv

script, user_name, password = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name,script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

#3. Add another argument and use it in your script.
print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice. And you password is %r
""" %(likes,lives,computer,password)


#4. Make sure you understand how Zed combined a """ style multi-line string with the % format activator as the last print.

#""" some code in between """ and ''' some code in between ''' have the same effects, the only difference is the styling.