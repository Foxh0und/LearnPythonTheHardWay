from nose.tools import *
from ex49 import lexicon
from ex49 import parser

def test_peek():
    lWordList = lexicon.scan( 'princess' )
    assert_equal( parser.peek( lWordList ), 'Noun' )
    assert_not_equal( parser.peek( lWordList ), 'Verb' )
    assert_equal( parser.peek( None ), None )

def test_match():
    lWordList = lexicon.scan( 'princess up down' )
    assert_equal( parser.match(lWordList, 'Noun'), ( 'Noun', 'princess' ) )
    assert_equal( parser.match(lWordList, 'Stop' ), None )
    assert_not_equal( parser.match( lWordList, 'Direction' ), ( 'Noun', 'up' ) )
    assert_equal( parser.match( None, 'Noun' ), None )

def test_skip():
    lWordList = lexicon.scan('bear eat door')
    assert_equal(lWordList, [('Noun', 'bear'), ('Verb', 'eat'),
                             ('Noun', 'door')])
    parser.skip(lWordList, 'Noun')
    assert_equal(lWordList, [('Verb', 'eat'), ('Noun', 'door')])

def test_parseVerb():
    lWordList = lexicon.scan( 'it eat door' )
    assert_equal( parser.parseVerb( lWordList ), ( 'Verb', 'eat' ) )
    lWordList = lexicon.scan( 'bear eat door' )
    assert_raises( parser.ParserError, parser.parseVerb, lWordList )

def test_parseobject():
    lWordList = lexicon.scan( 'the door' )
    assert_equal( parser.parseObject( lWordList ), ( 'Noun', 'door' ) )
    lWordList = lexicon.scan( 'the east' )
    assert_equal( parser.parseObject( lWordList ), ( 'Direction', 'east' ) )
    lWordList = lexicon.scan( 'the it' )
    assert_raises( parser.ParserError, parser.parseObject, lWordList )

def test_parsesubject():
    lWordList = lexicon.scan( 'door eat' )
    assert_equal( parser.parseObject( lWordList ), ( 'Noun', 'door' ) )

def test_parseSubject():
    lWordList = lexicon.scan( 'the bear eat the door' )
    lSentence = parser.parseSentence( lWordList )
    assert_equal( lSentence.fSubject, 'bear' )
    assert_equal( lSentence.fVerb, 'eat' )
    assert_equal( lSentence.fObject, 'door' )
