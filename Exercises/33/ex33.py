lCount = 0
lNumbers = []

while lCount < 6:
    print( f"At the top of i is {lCount}" )
    lNumbers.append( lCount )

    lCount += 1
    print( "Numbers now: ", lNumbers )
    print( f"At the bottom i is {lCount}" )

print( "The Numbers: ")

for i in lNumbers:
    print( i )
