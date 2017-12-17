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

  

        
