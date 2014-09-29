# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

class ParserError(Exception):
    pass

class Sentence(object):

    def __int__(self,subject,verb,object):
        # remember we take ('noun','princess') tuples and covert them
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = object[1]

# a way to "peek“ at a potential tuple so we can make some decisions.
def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

# a way to "match" different types of tuples that we expect in our subject-verb-object setup.
def match(word_list, expecting):
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

# a way to "skip" things we do not care about, like stop words.
def skip(word_list,word_type):
    while peek(word_list) == word_type:
        match(word_list,word_type)

def parse_verb(word_list):
    skip(word_list,'stop')
    if peek(word_list) == 'verb':
        return match(word_list,'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list,'stop')
    next = peek(word_list)
    if next == 'noun':
        return match(word_list,'noun')
    elif next == 'direction':
        return match(word_list,'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list,subj):
    verb = parse_verb(word_list)
    obj = parse_object(word_list)
    return Sentence(subj,verb,obj)


def parse_sentence(word_list):
    skip(word_list,'stop')

    start = peek(word_list)

    if start == 'noun':
        subj = match(word_list,'noun')
        return parse_subject(word_list,subj)
    elif start == 'verb':
        # assume the subject is the player then
        return parse_subject(word_list,('noun','player'))
    else:
        raise ParserError("Must start with subject, object, or verb not: %s" % start)
