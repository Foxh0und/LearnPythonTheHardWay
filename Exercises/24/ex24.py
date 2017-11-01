print( "Let's practise everything!" )
print( 'You\'d need to know \'bout escapes with \\ that do:' )

print( '\n newslines and \t tabs.')

poem = """
\t The lovely world
with logic so firmly planeted
cannot discern \n the needs of lovel
nor comprehend passion
and requres an explanation
\n\t\t where there is none.
"""

print( "--------" )
print( poem )
print( "--------" )

five = 10 - 2 + 3 - 6
print( f"This should be five: {five}" )

def getSecretFormula( aStartNumber ):
    lJellyBeans = aStartNumber * 500
    lJars = lJellyBeans / 1000
    lCrates = lJars / 100
    return lJellyBeans, lJars, lCrates

lStartNumber = 1000
lBeans, lJars, lCrates = getSecretFormula( lStartNumber )

print( "With a Startingpoint of: {}".format( lStartNumber ) )
print( f"We'd have {lBeans} beans, {lJars} jars, and {lCrates}, crates." )

lNewStartPoint = lStartNumber / 10

print( "We can also do it this way!" )

formula = getSecretFormula( lNewStartPoint )

print( "We'd have {} beans, {} jars and {} crates!".format(*formula) )
