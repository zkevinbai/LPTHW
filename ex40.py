class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
        # for line in, is a function that lets you read line by line 

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stopright there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

print "\n"

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

print "\n"
