from sys import exit

def endGame( aResult ):
        if aResult:
            print( "Thankyou master witcher!\nHere is your reward of 100 orens!" )
            exit()
        else:
            print( "Your journey comes to an end." )
            exit()

def wyvren():
    print( "You climb to the top of the tower and the wyveryn is circling overhead." )
    print( "You see two options:\n1. Cast Igni\n2. Jump at the wyvern" )


    lChoice = input( "> " )

    if lChoice == "1":
        print( "The wyvern crashes to the floor." )
        print( "1. Slash at the wyvrens throat\n2. Slash at the wyvrens head." )

        lChoice = input( "> " )

        if lChoice == "1":
            print( "Your strike hits deep into the monster, taking it's head clean off." )
            print( "You can return to the mayor to collect your reward" )
            endGame( True )
        else:
            print( "The wyvern dodges your blow, and you overswing, losing your balance." )
            print( "You trip over, and the monster throws it's claws, impaling and killing you." )
            endGame( False )


    else:
        print( "Your jump is short of the wyveryn and you plummet to your death!" )
        endGame( False )

def striga():
    print( "You make your way to the depths of the sewers finding the striga lying in wait" )
    print( "You see two options:\n1. Charge at the Striga\n2. Drink Cat" )


    lChoice = input( "> " )

    if lChoice == "2":
        print( "You can see clearly now, and the ground is very perilous" )
        print( "1. Slash at the Strigas throat\n2. Slash at the Strigas head." )

        lChoice = input( "> " )

        if lChoice == "1":
            print( "Your strike hits deep into the monster, taking it's head clean off." )
            print( "You can return to the mayor to collect your reward" )
            endGame( True )
        else:
            print( "The striga dodges your blow, and you overswing, losing your balance." )
            print( "You trip over, and the monster throws it's claws, impaling and killing you." )
            endGame( False )


    else:
        print( "You run blindly, and trip over falling down a small pit and drown in the waters below" )
        endGame( False )

def gryphen():
    print( "You make your way to the sunny fields, where not a thing is insight, until you hear the screams of the gryphen." )
    print( "You see two options:\n1. Shoot it with the crossbow\n2. Attempt to swing when it approaches" )


    lChoice = input( "> " )

    if lChoice == "1":
        print( "Your aim is true, and the gryphen crashes to the ground" )
        print( "1. Drive your sword into the fallen beasts heart\n2. Wait for the monster to get up and shoot again" )

        lChoice = input( "> " )

        if lChoice == "1":
            print( "Your strike hits deep into the monster, bursting its heart." )
            print( "You can return to the mayor to collect your reward" )
            endGame( True )
        else:
            print( "The monster is too clever, and flies away, knowing its beaten" )
            print( "You return to Kaer Morhen, as there will be no reward from the mayor" )
            endGame( False )


    else:
        print( "You run blindly, and trip over falling down a small pit and drown in the waters below" )
        endGame( False )

def start():
    print( "Greetings master witcher. Three problems are before the fair people of velen. Please choose one of the contracts to fulfill." )
    print( "1. Wyveryn in the tower.\n2. Striga in the sewers.\n3. Gryphen in the fields." )


    while( True ):
        lChoice = input( "> " )

        if lChoice == "1":
            wyvren()
        elif lChoice == "2":
            striga()
        elif lChoice == "3":
            gryphen()
        else:
            print( "Please choose a valid option, master withcer." )

start()
