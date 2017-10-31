from sys import argv

script, filename = argv

print( f"We're going to errase {filename} (if it exists)." )
print( "If you don't wish to do that, hit CTRL-C" )
print( "If you're happy to do that, press return" )

input( "?" )

print( "Opening the file..." )

target = open( filename, 'w' )

print( "Truncating the file. Goodbye!" )
target.truncate()

print( "Now I'm going to ask you for three lines." )

line1 = input( "line 1: " )
line2 = input( "line 2: " )
line3 = input( "line 3: " )

print( "I'm now going to write these to the file!" )

target.write( line1 )
target.write( "\n" )

target.write( line2 )
target.write( "\n" )

target.write( line3 )
target.write( "\n" )

print( "And finally we close the file.")
target.close()

print( "Let's take a look and see what's inside!" )

file = open( filename )
print( file.read() )

print( "See, it worked really well!" )
