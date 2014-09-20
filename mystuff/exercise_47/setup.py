# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description':'My Project',
    'author':'Jagger Kyne',
    'url':'http://jaggerkyne.com',
    'download_url':'Where to download it.',
    'author_email':'jagger.kyne@gmail.com',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['exercise.ex47'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)