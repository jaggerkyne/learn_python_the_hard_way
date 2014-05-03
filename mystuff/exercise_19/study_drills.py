#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# 1. Go back through the script and type a comment above each line, explaining in English what it does.

# 2. Start at the bottom and read each line backward, saying all the important characters.

# 3. Write at least one more function of your own design, and run it in 10 different ways.

def counting_people(children, men, women):
    print "There are %r children, %r men and %r women." % (children,men,women)
    print "Finish Counting."


counting_people(223,43,32)
counting_people(12/3,43,32)
counting_people(12*2,42,32)
counting_people(12%5,42,32)
counting_people(343,54/32,5)
counting_people(12%5,4/2,32)
counting_people(12%5,4*2,32)
counting_people(12%5,42,3%2)
counting_people(12%5,4*2,3%2)
counting_people(50,43*4,500%3)
# it is bad practice to have global variables and local variables share the same name.
# for practical purpose, we limits 5 arguments for a function.