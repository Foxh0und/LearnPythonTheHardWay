from Scenes import *

class Map( object ):

    fScenes = {
        "bridge": Bridge(),
        "northkorea": NorthKorea(),
        "pacificocean": PacificOcean(),
        "arctic": Arctic(),
        "success": Finish( True ),
        "failed": Finish( False ),
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
        fLastScene = self.fSceneMap.getNextScene( "finished" )

        while fCurrentScene != fLastScene:
            fNextScene = fCurrentScene.Play()
            fCurrentScene = self.fSceneMap.getNextScene( fNextScene )

        fCurrentScene.enter()


def Run():
    lMap = Map( "bridge" )
    lEngine = Engine( lMap )
    lEngine.play()

Run()
