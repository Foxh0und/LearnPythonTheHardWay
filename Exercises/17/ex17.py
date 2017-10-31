from sys import argv
from os.path import exists

script, from_file, to_file = argv

print( f"Copying from {from_file} to {to_file}." )

lInput = open(from_file).read()

print( f"The input file {len(lInput)} bytes long" )

print( f"Does the output file already exist? {exists(to_file)}" )
print("Read? Hit RETURN to continue or CTRL-C to abort." )

input()

lOutput = open( to_file, 'w' )
lOutput.write( lInput )

print("Alright, all done, just close the files now." )

lOutput.close()
