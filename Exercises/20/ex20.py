from sys import argv

script, input_file = argv

def print_all( aInput ):
    print( aInput.read() )

def rewind( aInput ):
    aInput.seek( 0 )

def printSpecificLine( aLineNumber, aInput ):
    print( aLineNumber, aInput.readline() )

lInput = open( input_file )

print( "First, let's print the whole file:\n" )
print_all( lInput )

print( "Now, let's go back to the beginning, just like rewinding a tape" )
rewind( lInput )

print( "Lets now print each line individually" )

lLineCounter = 1
printSpecificLine( lLineCounter, lInput )

lLineCounter += 1
printSpecificLine( lLineCounter, lInput )

lLineCounter += 1
printSpecificLine( lLineCounter, lInput )
