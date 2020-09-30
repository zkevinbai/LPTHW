# imports the argument variables given in the command line
from sys import argv

# unpacks argv, assigns its contents to the following 4 variables
script, first, second, third = argv

# prints the following arguments, calling on the contents of argv
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

'''
# combination drill

from sys import argv

script, I_have_cats = argv

print "The script is called:", script
print "you %s cats" %I_have_cats

cats = raw_input("How many cats do you have? ")

'''
