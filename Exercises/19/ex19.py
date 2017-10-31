## Note: I think it's time I used my own coding and naming conventions

def calculateCheeseAndCrackers( aCheeseCount, aBoxOfCrackerCount ):
    print(f"You have {aCheeseCount} pieces of cheese!" )
    print(f"And you have {aBoxOfCrackerCount} boxes of crackers!" )
    print( "That's enough for a party" )
    print( "Get a blanket.\n" )

print("We can just give the function numbers directly:" )
calculateCheeseAndCrackers( 20, 30 )

print( "Or we can use variables from our script:" )
lCheese = 10
lCrackers = 50
calculateCheeseAndCrackers( lCheese, lCrackers )

print( "We can even do math inside too: " )
calculateCheeseAndCrackers( 10 + 20, 5 - 2 )

print( "Finally, we can combine the two, variables and math:" )
calculateCheeseAndCrackers( lCheese + 100, lCrackers + 1000 )
