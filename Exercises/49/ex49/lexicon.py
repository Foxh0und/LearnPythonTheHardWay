lDirections = {'north',
              'south',
              'east',
              'west',
              'up',
              'down',
              'left',
              'right',
              'back'
              }
lVerbs = {'go',
          'stop',
          'kill',
          'eat'
          }

lStopWords = {'the',
              'in',
              'of',
              'from',
              'at',
              'it'
            }

lNouns = {'door',
          'bear',
          'princess',
          'cabinet'
          }

def definer( aInput ):
    lInput = aInput.lower()

    if lInput in lDirections:
        return ( 'Direction', aInput )
    elif lInput in lVerbs:
        return ( 'Verb', aInput )
    elif lInput in lStopWords:
        return ( 'Stop Word', aInput )
    elif lInput in lNouns:
        return ( 'Noun', aInput)
    elif aInput.isdigit():
        return ( 'Number', int( aInput ) )
    else:
        return ( 'Error' , aInput )

def scan( aInput ):
    lWords = aInput.split()
    return[definer( aWord ) for aWord in lWords]
