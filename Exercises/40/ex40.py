class Song(object):
    def __init__( self, aLyrics ):
        self.fLyrics = aLyrics

    def singSong( self ):
        print( self.fLyrics )


lBirthday = Song( "Happy Birthday to you..." )
lRage = Song( "The rally around the family..." )

lBirthday.singSong()
lRage.singSong()
