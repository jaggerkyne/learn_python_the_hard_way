# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


# What is the difference between a class and an object?
# Is similar as the difference between a Fish and a Salmon?

# A Salmon is a particular kind of Fish.

# Example, a bucket of three salmon, named Joe, Mary, Ken.
# What is the difference between Joe and Salmon?
# Joe is an instance of of Salmon.

# Fish is a class, -- not a real thing, but rather a word we attach to instances of things with similar attributes.
# Salmon is a class, -- a particular kind of fish.
# Joe is an object. -- a particular case of Salmon.

# Use two catchy phrases:
# 1. "is-a" ----> when you talk about objects and classes being
#                   related to each other by a class relationship.
# 2. "has-a"----> when you talk about objects and classes that are related
#                   only because they reference each other.

## Animal is-a object (Yes, sort of confusing) look at the extra credit

class Animal(object):
    def __init__(self,name,legs):
        self.name = name
        self.legs = legs

    def get_name(self):
        print "The name of animal is %s." % self.name

class Book():
    pass

## Dog is-an animal
class Dog(Animal):
    def __init__(self,name,legs):
        ## Dog has a name
        super(Dog,self).__init__(name,legs)


## Cat is-an animal
class Cat(Animal):
    def __init__(self,name,legs):
        super(Cat,self).__init__(name,legs)
        ## cat has-a name
        # self.name = name

## Person is-an object
class Person(object):
    def __init__(self,name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None # make sure self.pet is set to default of None.

## Employee is-a person
class Employee(Person):
    def __init__(self,name,salary):
        ## ?? hmm what is this strange magic?
        ## Employee has-a name.
        super(Employee,self).__init__(name)
        ## Employee has-a salary
        self.salary = salary

## Fish is-an object
class Fish(object):

    def swim(self):
        print "I am swimming in the ocean!"


## Salmon is-a Fish
class Salmon(Fish):

    def jump(self):
        print "I am a Salmon and I can jump!"

## Halibut is-a Fish
class Halibut(Fish):

    def sing(self):
        print "I am a Halibut and I can sing!"

## rover is-a Dog
rover = Dog("Rover",4)
print "My name is %s and I have %d legs." % (rover.name,rover.legs)

## satan is-a Cat
satan = Cat("Satan",4)
print "My name is %s and I have %d legs." % (satan.name,satan.legs)
# print "Cat's name is %s" % satan.name
## mary is-a Person
mary = Person("Mary")
print "My name is %s." % mary.name

## mary has a pet called satan
mary.pet = satan
print "My name is %s and I have a pet named %s." % (mary.name,satan.name)



## frank is-an employee has salary of 120000
frank = Employee("Frank",120000)

## frank has-a pet called rover
frank.pet = rover
print "My name is %s and I make %d a year, I have a pet call %s." % (frank.name,frank.salary,rover.name)

## flipper is-a Fish
flipper = Fish()
flipper.swim()
## crouse is-a Salmon
crouse = Salmon()
crouse.swim()
crouse.jump()
## harry is-a Halibut
harry = Halibut()
harry.swim()
harry.sing()
# Study Drills

# 1. Research why Python added this strange object class and what that means.
# a new way of declaring a class which inherits from object class.

# 2. Is it possible to use a class like it's an object?
# Yes.

# 3. Fill out the animals, fish, and people in this exercise with functions that
# make them do things. See what happens when functions are in a "base class"
# like Animal versus Dog.

# 4. Find other people's code and work out all the is-a and has-a relationships.

# 5. Make some new relationships that are lists and dicts so you can also
# have "has-many" relationships.

# Read "is-many" relationship and try to avoid is-many relationship as possible.
# read about multiple inheritance.

# Search "python super"
# A bit of formal
# http://www.artima.com/weblogs/viewpost.jsp?thread=236275
# More clear:
# http://blog.timvalenta.com/2009/02/understanding-pythons-super/