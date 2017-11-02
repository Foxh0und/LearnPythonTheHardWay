def breakWords( aInput ):
    """This function will break up words for us."""
    return aInput.split( ' ' )

def sortWords( aInput ):
    """Sorts the words."""
    return sorted( aInput )

def printFirstWord( aInput ):
    """Prints the first word after popping it off."""
    print( aInput.pop( 0 ) )

def printLastWord( aInput ):
    """Prints the last word after popping it off."""
    print ( aInput.pop( -1 ) )

def sortSentence( aInput ):
    """Takes in a full sentence and returns the sorted words."""
    return sortWords( breakWords( aInput ) )

def printFirstAndLastWords( aInput ):
    """Prints first and last words of a sentence"""
    lSplit = breakWords( aInput )
    printFirstWord( lSplit )
    printLastWord( lSplit )

def printFirstAndLastWordsSorted( aInput ):
        """Prints first and last words of a sentence"""
        lSplit = sortSentence( aInput )
        printFirstWord( lSplit )
        printLastWord( lSplit )
