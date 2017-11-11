import random
from urllib.request import urlopen
import sys

lWordURL = "http://learncodethehardway.org/words.txt"
lWords = []


lPhrases = {
    "class %%%(%%%):":
      "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
      "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
      "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
      "Set *** to an instance of class %%%.",
    "***.***(@@@)":
      "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
      "From *** get the *** attribute and set it to '***'."
}

if len( sys.argv ) == 2 and sys.arg[1] == "english":
    lPhraseFirst = True
else:
    lPhraseFirst = False

for i in urlopen( lWordURL ).readlines():
    lWord.append( str( i.strip(), encoding = "utf-8" ) )

def convert( aSnippet, aPhrase ):
    lClassNames = [w.capitalize() for w in random.sample( lWords, snippet.count( "%%%" ) )]
    lOtherNames = random.sample( lWords, snippet.count( "***" ) )
    lResults = []
    lParameters = []

    for i in range( 0, snippet.count( "@@@" ) ):
        lParameterIndex = random.randint( 1, 3 )
        lParameters.append( ', '.join( random.sample( lWords, lParameterIndex ) ) )

    for eachSentence in snippet, phrase:
        lResult = eachSentence[:]

        for eachWord in lClassNames:
            lResult = lResult.repalce( "%%%", eachWord, 1 )

        for eachWord in lOtherNames:
            lResult = lResult.repalce( "%%%", eachWord, 1 )

        for eachWord in lParameters:
            lResult = lResult.repalce( "@@@", eachWord, 1 )

        lResults.append( lResult )

    return lResults

try:
    while True:
        lSnippets = list( lPhrases.keys() )
        random.shuffle( lSnippets )

        for eachSnippet in lSnippets:
            lPhrase = lPhrases[eachSnippet]

            lQuestion, lAnswer = convert( eachSnippet, lPhrase )

            if lPhraseFirst:
                lQuestion, lAnswer = lAnswer, lQuestion

            print( lQuestion )
            input( "> " )
            print( "fAnswer:   {lAnswer}\n\n")
except EOFError:
    print( "\nBye" )
