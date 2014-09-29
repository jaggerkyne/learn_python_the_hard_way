# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


direction_words = ['north','south','east','west','down','up','left','right','back']
verbs = ['go','stop','kill','eat']
stop_words = ['the','in','of','from','at','it']
nouns = ['door','bear','princess','cabinet']

def convert_number(s):
        try:
            return int(s)
        except ValueError:
            return None

def scan(sur_input):

    # get user input
    stuff = raw_input(">")
    words = stuff.split()

    # empty bucket for list
    result_list = []

    # go through the list and test each word
    # to find out their category and return in this form: [(Category1, Word1)]

    for word in words:
        if word.lower() in direction_words:
            sentence = ('direction',word)
            result_list.append(sentence)
        elif word.lower() in verbs:
            sentence = ('verb',word)
            result_list.append(sentence)
        elif word.lower() in stop_words:
            sentence = ('stop',word)
            result_list.append(sentence)
        elif word.lower() in nouns:
            sentence = ("noun",word)
            result_list.append(sentence)
        elif word.isdigit():
            sentence = ("number",convert_number(word))
            result_list.append(sentence)
        else:
            sentence = ("error",word)
            result_list.append(sentence)
    return result_list



