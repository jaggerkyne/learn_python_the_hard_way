# --coding: utf-8 --
# Another code written by Jagger Kyne
# Copyright 2006 - 2014 Jagger Kyne <jagger.kyne@gmail.com>
__author__ = 'Jagger Kyne'


class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics # use self here makes more clear that is the local variable lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(['Happy birthday to you',
                   "I don't want to get sued",
                   "So I will stop right here"])

bulls_on_parade = Song(['They rally around the family',
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Study Drills

# 1. Write some more songs using this, and make sure you understand that you're passing
# a list of strings as the lyrics.

moutain_top = Song([u"这是一首歌！",
                    "what is this?"])

moutain_top.sing_me_a_song()


# 2. Put the lyrics in a separate variable, then pass that variable to the class to use instead.

song_lyrics = [u"主你是我最知心的朋友！",
               u"你把我从尘土中高举！"]

praise_lord = Song(song_lyrics)

praise_lord.sing_me_a_song()

some_thin_interesting = "This is my song to you!"

some_song = Song(some_thin_interesting)

some_song.sing_me_a_song() # treat the strings as a list.

# 3. See if you can hack on this and make it do more things. Don't worry if you have no idea
# how, just give it a try, see what happens. Break it, trash it, thrash it, you can't hurt it.

# 4. Search online for "Object-Oriented Programming" and try to overflow your brain with
# what you read. Don't worry if it make absolutely no sense to you. Half of that stuff makes
# no sense to me either.