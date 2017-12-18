from nose.tools import *
from ex47.game import Room

def test_room():
    lTestRoom = Room( "GoldRoom",
                      """This room has gold in it you can grab.
                      There's a door to the north.""")
    assert_equal( lTestRoom.fName, "GoldRoom" )
    assert_equal( lTestRoom.fPaths, {} )

def test_room_paths():
    lCenter = Room( "Center", "Test room in the center." )
    lNorth = Room( "North", "Test room in the north." )
    lSouth = Room( "South", "Test room in the south." )

    lCenter.addPaths( {'north': lNorth, 'south': lSouth} )
    assert_equal( lCenter.go( 'north' ), lNorth )
    assert_equal( lCenter.go( 'south' ), lSouth )

def test_map():
    lStart = Room( "Start", "You can go west and down a hole" )
    lWest = Room( "Trees", "There are trees down here, you can go east" )
    lDown = Room( "Dungeon", "It's dark down here, you can go up!" )

    lStart.addPaths( {"west": lWest, "down": lDown} )
    lWest.addPaths( {"east": lStart} )
    lDown.addPaths( {"up": lStart} )

    assert_equal( lStart.go( "west" ), lWest )
    assert_equal( lStart.go( "west" ).go( "east" ), lStart )
    assert_equal( lStart.go( "down" ).go( "up" ), lStart )
