lCount = [1, 2, 3, 4 ,5]
lFruits = ['apples', 'oranges', 'pears', 'apricots']
lChange = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for i in lCount:
    print( f"This is count {i}" )

for i in lFruits:
    print( f"A fruit of type: {i}" )

for i in lChange:
    print( f"I got {i}")

lElements = []

for i in range( 0, 6 ):
    print( f"Adding {i} to the list" )
    lElements.append( i )

for i in lElements:
    print( f"Element was: {i}" )
