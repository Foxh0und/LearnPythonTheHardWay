from sys import argv

script, filename = argv

txt = open( filename )
print( "Here is your file {filename}:" )

print( txt.read() )

print( "Type the filename again:" )
file = input( "> " )

print( open(file).read() )
