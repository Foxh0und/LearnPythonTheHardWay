class Parent( object ):
    def altered( self ):
        print( "Parent Altered" )

class Child( Parent ):

    def altered( self ):
        print( "Child before calling super" )
        super( Child, self ).altered()
        print( "Child after calling super" )

dad = Parent()
son = Child()

dad.altered()
son.altered()
