print "define x"
x = int(raw_input())
print "x squared is"
print x**2

print "How old are you?",
age = raw_input()
#print "Is that years, months or days?",
#age_unit = raw_input()
print "How tall are you?",
height = raw_input()
#print "Is that feet or meters?",
#height_unit = raw_input()
print "How much do you weigh?",
weight = raw_input()
#print "Is that pounds or kilograms?",
#weight_unit = raw_input()

print "So, you're %r old, %r tall and %r heavy." % (
    age, height, weight)

#print "So, you're %r %r old, %r %r tall and %r %r heavy." % (
#    age, age_unit, height, height_unit, weight, weight_unit)
