class Scene( object ):

    def enter( self ):
        pass

class Engine( object ):

    def __init__( self, aSceneMap ):
        pass

    def play( self ):
        pass

class Death( Scene ):

    def enter( self ):
        pass

class CentralCorridor( Scene ):

    def enter( self ):
        pass

class LaserWearponArmory( Scene ):

    def enter( self ):
        pass

class TheBridge( Scene ):

    def enter( self ):
        pass

class EscapePod( Scene ):

    def enter( self ):
        pass

class Map( object ):

    def __init__( self, aStartScene ):
        pass

    def getNextScene( self, aSceneName ):
        pass

    def getOpeningScene( self ):
        pass

lTempMap = Map( 'Central Coridor' )
lTempGame = Engine( lTempMap )
lTempGame.play()
