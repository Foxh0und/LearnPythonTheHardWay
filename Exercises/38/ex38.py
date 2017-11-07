lTenThings = "Apples Oranges Crows Telephone Light Sugar"

print( "Wait, there are not ten things in that list. Let's fix that." )

lSplit = lTenThings.split( ' ' )

lMoreStuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len( lSplit ) != 10:
    lNextOne = lMoreStuff.pop()
    print( "Adding: ", lNextOne )
    lSplit.append( lNextOne )
    print( f"There are now {len(lSplit)} things now." )

print( "There we go: ", lSplit )
print( "Lets do some things with it!" )

print( lSplit[1] )
print( lSplit[-1] )
print( lSplit.pop() )
print( ' '.join( lSplit ) )
print( '#'.join( lSplit[3:5] ) )
