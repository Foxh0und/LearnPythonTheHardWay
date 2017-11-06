from sys import exit

def goldRoom():
    print( "This room is full of gold. How much do you take?" )
    lChoice = input( "> " )

    if "0" in lChoice or "1" in lChoice:
        if( int( lChoice ) < 50 ):
            print( "Nice, you're not greedy, you win!" )
            exit( 0 )
        else:
            dead( "You greedy bastard!" )
    else:
        dead( "Man, learn to type a number!" )

def bearRoom():
    print( "There is a bear in here!" )
    print( "The bear has a pot of honey." )
    print( "The bear is front of another door." )
    print( "How are you going to move the bear?" )

    lBearMoved = False;

    while True:
        lChoice = input( "> " )

        if lChoice == "take honey":
            dead( "The bear looks at you then slaps your face off." )
        elif lChoice == "taunt bear" and not lBearMoved:
            print( "The bear has moved from the door, you may proceed." )
            lBearMoved = True;
        elif lChoice == "taunt bear" and lBearMoved:
            dead( "The bear gets pissed off and chews your legs off." )
        elif lChoice == "open door" and lBearMoved:
            goldRoom()
        else:
            print( "I got no idea what that means!" )

def cthulhuRoom():
    print( "Here you see the great eveil Cthulhu." )
    print( "He, it, whatever stares at you and you go insane." )
    print( "Do you flee for your life or eat your head?" )

    lChoice = input( "> " )

    if "flee" in lChoice:
        start()
    elif "head" in lChoice:
        dead( "Well, that was tasty!" )
    else:
        cthulhuRoom()

def dead( aReason ):
    print( aReason, "Thanks for playing!" )
    exit(0)

def start():
    print( "You are in a dark room." )
    print( "There is a door to your right, and a door to your left." )
    print( "Which one do you take?" )

    lChoice = input( "> " )

    if lChoice == "left":
        bearRoom()
    elif lChoice == "right":
        cthulhuRoom()
    else:
        dead( "You stumble around until you starve too death!" )

start()
