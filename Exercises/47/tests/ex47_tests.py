from nose.tools import *
from ex47.game import Room

def test_room():
    lTestRoom = Room( "GoldRoom",
                      """This room has gold in it you can grab.
                      There's a door to the north.""")
    assert_equal( lTestRoom.fName, "GoldRoom" )
    assert_equal( lTestRoom.fPaths, {} )
