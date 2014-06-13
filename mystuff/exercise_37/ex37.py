#--coding: utf-8 --
#Another code written by Jagger Kyne
#Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

#
# def keyword_and():
#
#     wisdom = 20
#     gold = int(raw_input("What is the gold you want?"))
#
#     ### -->  both side of the keyword end must be true before the code after it can be executed.
#     if gold >= 10 and wisdom == 20:
#         print "I have " + str(gold) + " pcs of gold."

# keyword_and()
#
# def keyword_del():
#     fruits = ['apple', 'pear', 'peach','orange']


####### Keywords #######
### -->  | and      | -> both side of operand must be true

### -->  | del      | -> This is a way to remove an item from a list given its index instead of its value.
                        # --> eg: a = [-1,1,66.06,333]
                        #           del a[0]
                        #         a = [1,66.06,333]

### -->  | from     | -> from a package

### -->  | not      | -> not

### -->  | while    | -> while loop

### -->  | as       | -> We use the as keyword, if we want to give a module a different alias
                        # http://zetcode.com/lang/python/keywords/

### -->  | elif     | -> other condition, after usage of if - elif and else block

### -->  | global   | -> access variables defined outside functions
                        # n most cases where you are tempted to use a global variable,
                        # it is better to utilize a parameter for getting a value into a function or
                        # return value to get it out.
                        # -> http://www.python-course.eu/python3_global_vs_local_variables.php

### -->  | or       | -> either side of operand be true

### -->  | with     | -> The above with statement will automatically close the file after the nested block of code.
                        # The advantage of using a with statement is that it is guaranteed to close the file
                        # no matter how the nested block exits.
                        # --> eg: http://preshing.com/20110920/the-python-with-statement-by-example/
                        # --> another explanation I think is better: http://effbot.org/zone/python-with-statement.htm

### -->  | assert   | -> Assert statements are a convenient way to insert debugging assertions into a program
                        # --> https://docs.python.org/release/2.5.2/ref/assert.html
                        # Assert statements check a condition,
                        # if it is true it does nothing, and if it is false it raises an
                        # AssertionError with an optional error message.
                        # Wrong way to use assert: https://mail.python.org/pipermail/python-list/2013-November/660401.html

### -->  | else     | -> if-elif-else

### -->  | if       | -> if statement to check the condition

### -->  | pass     | -> place holder to get python interpreter to let go

### -->  | yield    | -> is used with generators

### -->  | break    | -> interrupt the (loop) cycle, if needed

### -->  | except   | -> catches the exception and executes codes

### -->  | import   | -> import other modules into a Python script

### -->  | print    | -> print to console

### -->  | class    | -> used to create new user defined objects

### -->  | exec     | -> executes Python code dynamically

### -->  | in       | -> inside of some object?

### -->  | raise    | ->1. It's used for raising some errors.
                        # eg:
                        # if something:
                        #   raise error("My error!")
                    # ->2.The second is to reraise the current exception in an exception handler,
                    # so that it can be handled further up the call stack.
                        #eg:
                        #try:
                        #   generate_exeception()
                        #except SomeException, e:
                        #   if not can_handle(e):
                        #       raise
                        #   handle_exception(e)
                        #
### -->  | continue | -> used to interrupt the current cycle, without jumping out of the whole cycle.
                        # New cycle will begin.

### -->  | finally  | -> is always executed in the end. Used to clean up resources.

### -->  | is       | -> tests for object identity

### -->  | return   | -> exits the function and returns a value

### -->  | def      | -> used to create a new user defined function

### -->  | for      | -> iterate over items of a collection in order that they appear

### -->  | lambda   | -> creates a new anonymous function

### -->  | try      | -> specifies exception handlers

####### Data Types #######
### -->  | True     | -> condition is true

### -->  | False    | -> condition is incorrect

### -->  | None     | -> means non existent, not known or empty. equivalent to NULL

### -->  | strings  | -> String is a data type representing textual data in computer programs

### -->  | numbers  | -> integer eg: whole number like 12

### -->  | floats   | -> decimal number like 12.0

### -->  | lists    | -> A list is a mutable sequence data type.

####### String Escape Sequences #######
### -->  \\  -> Backslash(\)
### -->  \'  -> Single quote (')
### -->  \"  -> Double quote (")
### -->  \a  -> ASCII Bell (BEL)
### -->  \b  -> ASCII Backspace (BS)
### -->  \f  -> ASCII Formfeed (FF)
### -->  \n  -> ASCII Linefeed (LF)
### -->  \r  -> ASCII Carriage Return (CR)
### -->  \t  -> ASCII Horizontal Tab (TAB)
### -->  \v  -> ASCII Vertical Tab (VT)

####### String Formats or Interpolation #######
### -->  %d  --> Signed integer decimal
### -->  %i  --> Signed integer decimal
### -->  %o  --> Signed octal value
### -->  %u  --> Obsolete type - it is identical to 'd'
### -->  %x  --> Signed hexadecimal (lowercase)
### -->  %e  --> Floating point exponential format (lowercase)
### -->  %E  --> Floating point exponential format (uppercase)
### -->  %f  --> Floating point decimal format
### -->  %F  --> Floating point decimal format
### -->  %g  --> Floating point format. Uses lowercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
### -->  %G  --> Floating point format. Uses uppercase exponential format if exponent is less than -4 or not less than precision, decimal format otherwise.
### -->  %c  --> Single character (accepts integer or single character string).
### -->  %r  --> String (converts any Python object using repr()).
### -->  %s  --> String (converts any Python object using str()).
### -->  %%  --> No argument is converted, results in a '%' character in the result.

####### Operators #######

    ### Arithmetic Operators: ###
### -->  |   +   |  -> Addition - Adds values on either side of the operator
                        # --> eg: 5 + 6 = 100

### -->  |   -   |  -> Subtraction - subtracts right hand operand from the left hand operand
                        # --> eg: 7 - 3 = 4

### -->  |   *   |  -> Multiplication - multiples values on either side of the operator
                        # --> eg: 7 * 7 = 49

### -->  |   **  |  -> Exponent - performs exponential (power) calculation on operators
                        # --> eg: 4 ** 2 = 4^2 = 16

### -->  |   /   |  -> Division - Divides left hand operand by right hand operand
                        # --> eg: 16 / 4 = 4

### -->  |   //  |  -> Floor Division - The division of operands where the result is the quotient in which the
                       # digits after the decimal point are removed.
                        # --> eg: 9//2 is equal to 4 and 9.0//2.0 is equal to 4.0

### -->  |   %   |  -> Modulus - Divides left hand operand by right hand operand the returns remainder.
                        # --> eg: 9 % 4 = 1



    ### Comparison Operators ###
### -->  |   <   | -> checks if the value of left operand is less than the value of the right operand,
                        # if yes then condition becomes true.
                        # --> eg: (a < b) is true.

### -->  |   >   | -> checks if the value of left operand is greater than the value of right operand,
                        # if yes then condition becomes true.
                        # --> eg: (a > b) is not true.

### -->  |   <=  | -> checks if the value of left operand is less or equal to the value of right operand,
                        # if yes then condition becomes true.
                        # --> eg: (a <= b) is true.

### -->  |   >=  | -> checks if the value of left operand is greater or equal to the value of right operand,
                        # if yes then condition becomes true.
                        # --> eg: (a >= b) is not true.

### -->  |   ==  | -> checks if the value of two operands are equal or not, if yes, return True; if not return False.
                        # --> eg: (a==b) is not true

### -->  |   !=  | -> checks if the value of two operands are equal or not, if values are not equal then
                        # condition becomes True.
                        # --> eg: (a!=b) is true

### -->  |   <>  | -> checks if the value of two operands are equal or not, if values are not equal
                        # then condition becomes true.
                        # --> eg: (a<>b) is true. This is similar to != operator.

### -->  |   ()  | -> ()

### -->  |   []  | -> list

### -->  |   {}  | -> tuple or code

### -->  |   @   | --> Python Decorator http://www.artima.com/weblogs/viewpost.jsp?thread=240808

# Python Decorators allow you to inject or modify functions or classes, and in the case of class decorators, entire classes.
# The only constraint upon the object returned by the decorator is that it can be used as a function --
# which basically means it must be callable. Thus, any classes we use as decorators must implement __call__.
# TODO still not quite understand what Python Decorators mean, need to look into more.
### -->  |   ,   |

### -->  |   :   | --> ":" marks the beginning of the class, method, conditions details:
                        # --> eg: if a < = b:
                        #            a += b

### -->  |   .   | --> "." dot operator, it invokes methods or golbal variables of an object it calls.
                        # --> eg: person.eat()

####Assignment Operators ####

### -->  |   =   | --> Simple assignment operator. Assigns values from right side operands to left side operand.
                    # --> eg: c = a + b will assigns value of a + b into c

### -->  |   +=  | --> Add AND assignment operator, it adds right operand to the left operand and
                        # assign the result to left operand.
                    # --> eg: c += a is equivalent to c = c + a

### -->  |   -=  | --> Subtract and assignment operator, it subtracts right operand from the left operand and
                        # assign the result to left operand.
                    # --> eg: c -= a is equivalent to c = c - a

### -->  |   *=  | --> Multiply and assignment operator, it multiplies right operand from the left operand and
                        # assign the result to left operand.
                    # --> eg: c *= a is equivalent to c = c * a

### -->  |   /=  | --> Divide and assignment operator, it divides right operand from the left operand and
                        # assign the result to left operand.
                    # --> eg: c /= a is equivalent to c = c / a

### -->  |   //= | --> Floor Division and assigns a value, Performs floor division on operators and
                        # assign the result to left operand.
                    # --> eg: c //= a is equivalent to c = c // a

### -->  |   %=  | --> Modulus and assignment operator, it takes modulus using two operands and
                        # assign the result to left operand.
                    # --> eg: c %= a is equivalent to c = c % a

### -->  |   **= | --> Exponent and assignment operator, performs exponential (power)  calculation on operators and
                        # assign the result to left operand.
                    # --> eg: c **= a is equivalent to c = c ** a

#### Separator ####

### -->  |   ;   | -> used at the end of each statement, also used when you want to put several
                        # statements on the same line.
                    # --> eg: a = b;c = d; f = 19 - f
