def add(a, b):
    print "ADDING %d + %d" % (a,b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "MULTIPLYING %d / %d" % (a, b)
    return a * b

def divide(a, b):
    print "DIVIDING %d / %d" % (a, b)
    return a / b

print "\nLet's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "\nmore math"
add(1, 1)
x = subtract(add(24, divide(34, 100)), 1023)
print x

# A puzzle for the extra credit, type it in anyway.
print "\nHere is a puzzle."

what = subtract(age, add(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?\n"
