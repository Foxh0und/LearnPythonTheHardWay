from nose.tools import *
from ex48 import lexicon

def test_directions():
    assert_equal( lexicon.scan( "north" ), [( 'Direction', 'north' )] )
    lTempResult = lexicon.scan( "north south east")
    assert_equal( lTempResult, [('Direction', 'north'),
                                ('Direction', 'south'),
                                ('Direction', 'east')])

def test_verbs():
    assert_equal( lexicon.scan( "go" ), [( 'Verb', 'go')] )
    lTempResult = lexicon.scan( "go kill eat")
    assert_equal( lTempResult, [('Verb', 'go'),
                                ('Verb', 'kill'),
                                ('Verb', 'eat')])
def test_stops():
    assert_equal( lexicon.scan( "the" ), [( 'Stop Word', 'the')] )
    lTempResult = lexicon.scan( "the in of")
    assert_equal( lTempResult, [('Stop Word', 'the'),
                                ('Stop Word', 'in'),
                                ('Stop Word', 'of')])

def test_nouns():
    assert_equal( lexicon.scan( "bear" ), [( 'Noun', 'bear')] )
    lTempResult = lexicon.scan( "bear princess")
    assert_equal( lTempResult, [('Noun', 'bear'),
                                ('Noun', 'princess')])

def test_nouns():
    assert_equal( lexicon.scan( "1234" ), [( 'Number', 1234 )] )
    lTempResult = lexicon.scan( "3 91234")
    assert_equal( lTempResult, [('Number', 3),
                                ('Number', 91234)])

def test_stops():
    assert_equal( lexicon.scan( "ASDFADFASDF" ), [( 'Error', 'ASDFADFASDF')] )
    lTempResult = lexicon.scan( "go ISA princess")
    assert_equal( lTempResult, [('Verb', 'go'),
                                ('Error', 'ISA'),
                                ('Noun', 'princess')])
