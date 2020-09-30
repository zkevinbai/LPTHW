i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now: ", numbers
    print "At the bottom i is %d\n" % i


print "The numbers: "

for num in numbers:
    print num

# 1) Convert this while-loop to a function that you can call,
# and replace 6 in the test (i < 6) with a variable.

# 2) Add another variable to the function arguments that you can pass in that
# lets you change the + 1 on line 8 so you can change how much it increments by.

# mlut = make list up to
def mlut(number, increment):
    i = 0
    numbers = []

    while i < number:
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment
        print "Numbers now: ", numbers
        print "At the bottom i is %d\n" % i

# 3) Write it to use for-loops and range. Do you need the incrementor
# in the middle anymore? What happens if you do not get rid of it?
# > you can have the incrementor but it will require an usage of range syntax

# mlut_for = make list up to with for loop
def mlut_for(number, increment):
    i = 0
    numbers = []

    for i in range(0, number, increment):
        print "At the top i is %d" % i
        numbers.append(i)

        i += increment

        print "Numbers now: ", numbers

        print "At the bottom i is %d\n" % i
