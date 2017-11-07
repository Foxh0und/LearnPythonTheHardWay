lStates = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

lCities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

lCities['NY'] = 'New York'
lCities['OR'] = 'Portland'

print( '-' * 10 )
print( "NY state has: ", lCities['NY'] )
print( "OR state has: ", lCities['OR'] )
print( '-' * 10 )
print( "Michigan's abbreviation is: ", lStates['Michigan'] )
print( "Florida's abbreviation is: ", lStates['Florida'] )
print( '-' * 10 )

for state, abbr in list( lStates.items() ):
    print( f"{state} is abreivated {abbr}" )

print( '-' * 10 )

for state, city in list( lCities.items() ):
    print( f"{state} has the city {city}" )

print( '-' * 10 )


for state, abbr in list( lStates.items() ):
        print( f"{state} is abreivated {abbr}" )
        print( f" and has the city {lCities[abbr]}" )

print( '-' * 10 )

lState = lStates.get( "Texas" )

if not lState:
    print( "Sorry, no texas." )

lCity = lCities.get( 'TX', 'Does not exist' )
print( f"The city for the state 'TX' is: {lCity}" )
