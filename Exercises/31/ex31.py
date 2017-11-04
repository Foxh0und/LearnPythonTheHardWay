print( "You enter a dark room with two doors." )
print( "Do you go through door #1 or door #2?" )

door = input( "> " )

if door == "1":
    print( "There is a giant bear here eating a cheese cake." )
    print( "What do you do?" )
    print( "1. Take the cake." )
    print( "2. Scream at the bear" )

    bear = input( "> " )

    if bear == "1":
        print( "Oh no! The bear ate your face off!" )
    elif bear == "2":
        print( "Oh no! The bear ate your legs off!" )
    else:
        print( "Well doing {} is probably a safer option!".format(bear) )
        print( "Bear runs away!" )

elif door == "2":
    print( "You stare into the endless abyss." )
    print( "1. Blueberries" )
    print( "2. Yellow jacket clothespins." )
    print( "3. Understanding revolvers yelling melodies." )

    insanity = input( "> " )

    if insanity == "1" or insanity == "2":
        print( "Your body survives powered by a mind of jelly." )
        print( "Good Job!" )
    else:
        print( "Your insanity rots your eys into a pool of gunk." )
else:
    print( "You stumble around and fall on a knife!" )
