from Scenes import *

class Map( object ):

    fScenes = {
        "bridge": Bridge(),
        "northkorea": NorthKorea(),
        "pacificocean": PacificOcean(),
        "arctic": Arctic(),
        "yellowsea": YellowSea(),
        "seaofjapan": SeaOfJapan(),
        "honolulu": Honolulu(),
        "midway": Midway(),
        "success": Success(),
        "failed": Fail(),
    }

    def __init__( self, aStartScene ):
        self.fStartScene = aStartScene

    def getNextScene( self, aSceneName ):
        return Map.fScenes.get( aSceneName )

    def getOpeningScene( self ):
        return self.getNextScene( self.fStartScene )

class Engine( object ):

    def __init__( self, aSceneMap ):
        self.fSceneMap = aSceneMap

    def play( self ):
        fCurrentScene = self.fSceneMap.getOpeningScene()
        fLastScene = self.fSceneMap.getNextScene( "success" )


        while fCurrentScene != fLastScene:
            fNextScene = fCurrentScene.Play()
            fCurrentScene = self.fSceneMap.getNextScene( fNextScene )

        fCurrentScene.Play()


def Run():
    lMap = Map( "bridge" )
    lEngine = Engine( lMap )
    lEngine.play()

Run()
