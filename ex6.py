# assigns the string in quotations to the variable on the left
x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those %s." % (binary, do_not)

# prints the variables x and y
print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

# assings the false format to the hilarious variable
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

# prints a two sided string
print w + e
