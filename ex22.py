# There is no code needed this chapter, I just wanted to play around

'''
cats = int(raw_input("How mant cats do you have?"))
print "I have %d cats, and one tab before this period\n." % cats

from sys import argv
script, input_file = argv

current_file = open(input_file)

def print_a_line(line_count, f):
    print line_count, f.readline(),

print_a_line(1, current_file)

from sys import argv

script, input_file = argv

current_file = open(input_file)

def print_a_line(line_count, f):
    print line_count, f.readline(),

print "Let's print line1:"
# runs print a line 3 times for the 3 lines in the file
current_line = 1
print_a_line(1, current_file)
'''
