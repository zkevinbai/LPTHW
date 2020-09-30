"""
Write some more songs using this and make sure you understand that
you're passing a list of strings as the lyrics.

Put the lyrics in a separate variable, then pass that variable to
the class to use instead.

See if you can hack on this and make it do more things.
Don't worry if you have no idea how, just give it a try, see what happens.
Break it, trash it, thrash it, you can't hurt it.
"""

class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
        # pulls lyrics from self so you can do things to it 
    def print_song(self):
        print self.lyrics

new_song = Song(["No", "No", "No"])
# the things you pass into a class can be a string, tuple, list

new_song.print_song()
