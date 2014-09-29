# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


from nose.tools import *
from ..ex49 import parser


def test_parse_subject():
    assert_raises(parser.ParserError,parser.parse_subject,"next","next")


def test_parse_object():
    assert_raises(parser.ParserError,parser.parse_object,'kill')


def test_parse_verb():
    assert_raises(parser.ParserError,parser.parse_verb,"next")


