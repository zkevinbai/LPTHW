# uses argv to get a filename
from sys import argv

# unpacks argv into script and filename
script, filename = argv

# uses open command on file, converts it into the variable txt
txt = open(filename)

# prints the filename and then reads the file
print "Here is your file %r:" % filename
print txt().read

# prompts for the file again
print "Type the filename again:"
file_again = raw_input("> ")

# titles the variable txt_again as a command to open file_again
txt_again = open(file_again)

# reads txt_again
print txt_again.read()
