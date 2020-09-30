print "Lets's practice everything."
print "You\'d need to know \'bout escapes with \\ that do \n newline and \t tabs."

poem = '''
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from institution
and requires and explanation
\n\t\twhere there is none.
'''

print "_"*14
print poem
print "_"*14

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five

# defines secret_formula as a function which calculates three variables (beans,
# jars and crates) using the started variable and returns them
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

# identifies the start point and plugs it in to the started variable
start_point = 10000

# unpackes secret_formula
beans, jars, crates = secret_formula(start_point)

# uses the unpacked secret_formula to print
print "With a starting point of: %d" % start_point
print "We'd have %d beans, %d jars, and %d crates" % (beans, jars, crates)

start_point = start_point / 10

# uses the secret formula directly 
print "We can also do that this way:"
print "we'd have %d beans, %d jars, and %d crates" % secret_formula(start_point)
