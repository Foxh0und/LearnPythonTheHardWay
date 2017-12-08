from textwrap import dedent

class Scene( object ):

    def Play( self ):
        pass

    def processInput( self, aNumberOfChoice ):
        lChoice = input( "> " )

        while True:
            lChoice = int( lChoice )
            if( lChoice >= 1 and lChoice <= aNumberOfChoice ):
                return lChoice
            print( "Please enter a valid option." )
            lChoice = input( "> " )


class Bridge( Scene ):

    def Play( self ):
        Print( "Please enter your name" )
        lName = input( "> " )
        print( dedent( f"""
            Welcome aboard the USS Liberty. You mission Commander {lName},
            should your mission, should you choose to accept it, is to hunt
            down the North Korean warship, the NK Wonsan. According to our
            intelligence sources, the ship is carrying a nuclear ICBM, and is
            planning on using it. You must intercept the Wonsan and stop it at
            all costs!
            """) )

        print( "1. Proceed towards North Korea." )
        print( "2. Proceed through the Pacific Ocean" )
        print( "3. Proceed into the Arctic" )

        lOptions = { 1: "northkorea",
                     2: "pacificocean",
                     3: "arctic",
                    }
        return lOptions[super( Bridge, self).processInput( len( lOptions ) )]

class NorthKorea( Scene ):

    def Play( self ):
            print( dedent( """
                "You proceed towards North Korea, but do not detect any North
                Korean vessles anywhere, so you must keep going."
                """) )

            print( "1. Move to the west into the Yellow Sea" )
            print( "2. Continue into the Sea of Japan" )

            lOptions = { 1: "yellowsea",
                         2: "seaofjapan",
                        }
            return lOptions[super( NorthKorea, self).processInput( len( lOptions ) )]

class PacificOcean( Scene ):

    def Play( self ):
        print( dedent( """
            As you move into Pacific Ocean you are presented with two options.
            The National Guard based in Honolulu reports that several
            undocumented ships have docked, but cannot confirm if they are
            undercover enemy combatants, or members of the many pirate
            enterprises. Jones, the SONAR office tells you that there is a small
            signal coming from the island of midway.
            """) )

        print( "1. Dock in Honolulu" )
        print( "2. Proceed to Midway" )

        lOptions = { 1: "honolulu",
                     2: "midway",
                    }

        return lOptions[super( PacificOcean, self).processInput( len( lOptions ) )]

class Arctic( Scene ):

    def Play( self ):
                print( dedent( """
                    As you proceed through the Arctic, you are overcome with a
                    strange session. You move to the top of the deck to look
                    around. There is nothing as far as the eye can see besides
                    Ice, and you decide that you most definitely made a wrong
                    move here.

                    Almost momenterily, a communication from the Admirality
                    arrives, signalling that there have been several strange
                    vessels spotted in Hawaii, so you decide to head there.
                    """) )

                return "honolulu"

class YellowSea( Scene ):
    def Play( self ):
        print( dedent( """
            As you proceed into the yellow sea, an uneasy eariness
            comes over you and the rest of your ship. From a distance,
            you hear fighter jets approach.

            Your saliors scramble to react, but are not quick enough,
            and the ship is sunk. Many men die onboard, and the fate of
            the world is left to the mercy of the Wonsan.
            """) )

        return "failed"

class SeaOfJapan( Scene ):
    def Play( self ):
        print( dedent( """
            As you proceed into the Sea of Japan, Japanese ships quickly
            approach and blockade your ship. You have forgotten to
            notify the Japanese of your movments and have broken
            international law!

            Fortunately for you, the Japanese Prime Minister is very
            wary of North Korea, and understands the situation when
            presented with the facts. He directs you to keep moving with
            your mission, and states no ships have been found in the
            seas surrounding Japan and Korea.
            """ ) )


        print( "1. Proceed back to the Pacific Ocean" )
        print( "2. Proceed into the Arctic" )

        lOptions = { 1: "pacificocean",
                     2: "arctic",
                    }
        return lOptions[super( SeaOfJapan, self).processInput( len( lOptions ) )]

class Honolulu( Scene ):

    def Play( self ):
        print( dedent( """
                You pull into port at Honolulu and see that there are indeed
                many strange looking vessels. You slink off the ship and decide
                to have a look around.

                As you wander around the docks, you walk past a crying lady, and
                everywhere you look, people are gasping at their phones.

                San Francisco has been destroyed by a Nuclear Missile!

                You have failed to avert nuclear war!
                """ ) )

        return "failed"

class Midway( Scene ):

    def Play( self ):
        print( dedent( """
            As you approach Midway, the famed location of a decicive second
            war battle, you notice that there appears to be a base setup on the
            island.

            From a safe distance, you can see that the North Korean's are ready
            to launch missiles from their makeshift base!

            Fortunately for you, the President is on the line, and he authorises
            you too terminate the enemey with extreme prejudice. You quickly
            scramble the two F22 Raptors on board, who bomb the enemy until there
            is nothing left, saving the day!
            """ ) )

        return "success"

class Success( Scene ):
    def Play( self ):
        print( "Well done, you saved the day!" )
        exit( 0 )

class Fail( Scene ):
    def Play( self ):
        print( "Oh no, better luck next time !" )
        exit( 0 )
