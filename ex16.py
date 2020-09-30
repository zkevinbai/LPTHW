# this allows python to take input from the command line
from sys import argv

# script is automatically taken from the command line, you specify
# that you will not need script when unpacking
script, filename = argv

# gives prompts to the user and tells you what to do
# CTRL-C closes the python document, RETURN continues runing it
print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you want that, hit RETURN."

# asks what you want to do
raw_input("?")

# opens the file in the mode writing, which truncates the file
print "Opening the file..."
target = open(filename, 'w')

# truncates the file
print "Truncating the file. Goodbye!"
target.truncate()

# asks for text from the user
print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

# writes to the file on a new line
print "I'm going to write these to the file."

new_line = "\n"

target.write(line1 + '\n' + line2 + '\n' + line3 + '\n')

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# closes and saves the file
print "And finally, we close it."
target.close()


'''
# code to open a file
from sys import argv

script, filename = argv

text = open(filename,'r')

print text.read()
'''
