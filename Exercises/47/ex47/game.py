class Room( object ):

    def __init__( self, aName, aDescription ):
        self.fName = aName;
        self.fDescription = aDescription;
        self.fPaths = {}

    def go( self, aDirection ):
        return self.fPaths.get( aDirection, None)

    def addPaths( self, aPaths ):
        self.fPaths.update( aPaths )
