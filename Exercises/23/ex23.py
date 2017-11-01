import sys
script, encoding, error = sys.argv

def main( aInputFile, aEncodingType, aErrorFlag ):
    lLine = aInputFile.readline()

    if lLine:
        printline( lLine, aEncodingType, aErrorFlag )
        return main( aInputFile, aEncodingType, aErrorFlag )

def printline( aLine, aEncodingType, aErrorFlag ):
    lNextLang = aLine.strip()
    lRawBytes = lNextLang.encode ( aEncodingType, errors = aErrorFlag )
    lCookedString = lRawBytes.decode( aEncodingType, errors = aErrorFlag )
    print( lRawBytes, " <===> ", lCookedString )

lanaguages = open( "languages.txt", encoding = "UTF-8" )

main( lanaguages, encoding, error )
