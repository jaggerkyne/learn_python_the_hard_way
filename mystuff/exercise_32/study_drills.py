#--coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


#1. Take a look at how you used range. Look up the range function to understand it.

# tutorial on how to use range(): https://docs.python.org/release/1.5.1p1/tut/range.html

#2. Could you have avoided that for-loop entirely on line 22 and just assigned range(0,6) directly to elements?
# yes, but it take more lines to code
# range(0,6) gives a list of [0,1,2,3,4,5]
# then we pop the items in the list one by one
# then append the popped item into elements.

#3. Find the python documentation on lists and read about them. What other operations can you do to lists beside append?
# https://docs.python.org/2/tutorial/datastructures.html

####### list operations: ##########
# list.append(x): add an item to the end of the list
# list.extend(L): extend the list by appending all the items in the given list
# list.insert(index_of_the_element_before_which_to_insert,element_x): insert an item at a give position
# list.remove(x): remove the first item from the list whose value is x.
# list.pop([i]): remove the item at the given position in the list and return it. If not specific position is givem,
#  list.pop() removes and returns the last item in the list.
# list.index(x): return the index in the list of the first item whose value is x.
# list.count(x): return the number of times x appears in the list
# list.sort(): sort the items of the list in place.
# list.reverse():reverse the elements of the list in place.