# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'

from mystuff.exercise_45.engine import Engine
from mystuff.exercise_45.engine import Map

# starting point, the hall of choices.
a_map = Map('hall_of_choices')

# use the first map to create a game using Engine.
a_game = Engine(a_map)

# play the game.
a_game.play()
