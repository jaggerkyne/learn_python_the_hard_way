#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

print "\\" # only print out one \

print "I am 6'2\" tall." # use \" to escape double-quote inside string

print "I am 6\'2 tall." # use \' to escape single-quote inside string

##########################################################################
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

# remember escape sequences

#   Escape          What it does
#     \\                Backslash(\)
#     \'                Single-quote(')
#     \"                Double-quote(")
#     \a                ASCII bell(BEL)
#     \b                ASCII backspace(BS)
#     \f                ASCII formfeed(FF)
#     \n                ASCII linefeed(LF)
#     \N{name}          Character named name in the Unicode database(Unicode only)
#     \r                ASCII carriage return (CR) -> remove everything before \r
#     \t                ASCII horizontal tab (TAB)
#     \uxxxx            Character with 16-bit hex value xxxx (Unicode only)
#     \Uxxxxxxxx        Character with 32-bit hex value xxxxxxxx (Unicode only)
#     \v                ASCII vertical tab(VT)
#     \ooo              Character with octal value oo
#     \xhh              Character with hex value hh
#

# infinite loop, with cause the computer to crash.
# while True:
#      for i in ["/","-","|","\\","|"]:
#          print "%s\r" % i,

print "backslash %s." % "\\"

print "escape single-quote: %s." % "\'"

print "escape double-quote: %s." % "\""

print "escape ASCII Bell(BEL) %s." % "\a"

print "escape ASCII backspace(BS) %s..." % "\b"

print "escape ASCII formfeed(FF) %s..." % "\f"

print "escape ASCII linefeed(LF) %s..." % "\n"

print "escape Character named %s in the Unicode database " % "\N{好}"

print "escape ASCII carriage return(CR) %s..." % "\r"

print "escape ASCII horizontal tab(TAB) %s..." % "\t"

print "escape ASCII vertical tab(VT) %s..." % "\v"