def add( aLeftHandSide, aRightHandSide ):
    print(f"Adding {aLeftHandSide} and {aRightHandSide}.")
    return aLeftHandSide + aRightHandSide

def subtract( aLeftHandSide, aRightHandSide ):
    print( f"Subtracting {aLeftHandSide} and {aRightHandSide}." )
    return aLeftHandSide - aRightHandSide

def multiply( aLeftHandSide, aRightHandSide ):
    print( f"Multiplying {aLeftHandSide} and {aRightHandSide}." )
    return aLeftHandSide * aRightHandSide

def divide( aLeftHandSide, aRightHandSide ):
    print( f"Dividing {aLeftHandSide} and {aRightHandSide}." )
    return aLeftHandSide / aRightHandSide

print( "Now, let's do some maths with these functions!\n" )

age = add( 30, 5 )
height = subtract( 78, 4 )
weight = multiply( 35, 2 )
iq = divide( 200, 2 )

print( f"Age: {age}, height: {height}, weight: {weight}, IQ: {iq}." )

print( "Here is a puzzle!" )

what = add( age, subtract( height, multiply( weight, divide( iq, 2 ) ) ) )

print("That becomes: ", what )
