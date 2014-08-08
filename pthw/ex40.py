class Song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line
    
happy_bday = Song(["Happy birthday to me",
                   "Happy birthday to me",
                   "I guess this is enough"])

bulls_on_parade = Song(["This is the next one",
                        "That is suppose to sing"])
happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()