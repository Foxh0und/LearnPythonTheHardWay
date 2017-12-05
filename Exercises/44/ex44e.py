class Other( object ):

    def override( self ):
        print( "Other override" )

    def implicit( self ):
        print( "Other implicit" )

    def altered( self ):
        print( "Other altered" )

class Child( object ):

    def __init__( self ):
        self.fOther = Other()

    def implicit( self ):
        self.fOther.implicit()

    def override( self ):
        print( "Child override" )

    def altered( self ):
        print( "Child, Before other altered" )
        self.fOther.altered()
        print( "Child after other altered" )

son = Child()

son.implicit()
son.override()
son.altered()
