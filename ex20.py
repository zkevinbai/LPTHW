# imports argument variables from terminal
from sys import argv

# unpacks argv
script, input_file = argv

# defines print_all() as a function that reads a file
def print_all(f):
    print f.read()

# defines rewind() as a function that finds
def rewind(f):
    f.seek(0)

# defines print_a_line as a function that prints one line
def print_a_line(line_count, f):
    print line_count, f.readline(),

# identifies current_file as a variable which opens the input_file
current_file = open(input_file)

print "First let's print the whole file:"
# runs print_all on current_file
print_all(current_file)

print "Now let's rewind, kind of like a tape.\n"
# runs rewind on current_file
rewind(current_file)

print "Let's print 3 lines:"
# runs print a line 3 times for the 3 lines in the file
current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
