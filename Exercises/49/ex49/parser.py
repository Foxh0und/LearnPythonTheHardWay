class ParserError( Exception ):
    pass

class Sentence( object ):
    def __init_( self, aSubject, aVerb, aObject ):
        self.fSubject = aSubject[1]
        self.fVerb = aVerb[1]
        self.fObject = aObject[1]

def peek( aWordList ):
    if aWordList:
        return aWordList[0][0]
    else:
        return None

def match( aWordList, aExpectedType ):
    if aWordList:
        lWord = aWordList.pop( 0 )

        if lWord[0] = aExpectedType:
            return word
        else:
            return None
    else:
        return None

def skip( aWordList, aType ):
    while peek( aWordList ) == aType:
        match( aWordList, aType )

def parseVerb( aWordList ):
    skip( aWordList, 'Stop Word' )

    if peek( aWordlist ) == 'Verb':
        return match( aWordList, 'Noun' )
    else:
        raise PraserError( "Expected a noun or direction next" )

def parseObject( aWordList ):
    skip( aWordList, 'Stop Word' )

    lNextWord = peek( aWordList )

    if lNextWord == 'Noun':
        return match( aWordList, 'Noun' )
    elif lNextWord == 'Direction':
        return match( aWordList, 'Noun' )
    else:
        raise ParserError( "Expected a noun or direction next" )

def parseSubject( aWordList ):
    skip( wordList, 'Stop Word' )

    lNextWord = peek( aWordList )

    if lNextWord == 'Noun':
        return match( aWordList, 'Noun' )
    elif lNextWord == 'Verb':
        return ( 'Noun', 'player')
    else:
        raise ParserError( "Expected a verb next.")

def parseSentence( aWordList ):
    lSubject = parseSubject( aWordList )
    lVerb = parseVerb( aWordList )
    lObject = parseObject( aWordList )

    return Sentence( lSubject, lVerb, lObject )
