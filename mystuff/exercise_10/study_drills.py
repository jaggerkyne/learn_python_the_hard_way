#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# 1. Memorize all the escape sequences by putting them on flash cards.

# 2. Use '''(triple-single-quote) instead. Can you see why you might use that instead of """?

# 3. Combine escape sequences and format strings to create a more complex format.

# 4. Remember the %r format? Combine %r with double-quote and single-quote escapes and print them out.
# compare %r with %s.
# Notice how %r prints it the way you'd write it in your file, but %s prints it the way you'd like to see it?
# single-quotes and double-quotes are the same effect in this case.

print '''

This is a combinations of escapes values:

Something in here \n more than \t and \r vegetable.
I love \fEsther Liu, \vthis is a \atrue and \bnothing.
More than anything \r%s, my \vlove is %r.
''' % ("Truth","You")

print "*" * 20

print """

This is a combinations of escapes values:

Something in here \n more than \t and \r vegetable.
I love \fEsther Liu, \vthis is a \atrue and \bnothing.
More than anything \r%s, my \vlove is %r.
""" % ("Truth","You")

# %r is for debugging and %s is for displaying.

# using ''' or """ depends on the style chosen by the developing group.
