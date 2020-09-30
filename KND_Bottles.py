# version 1
"""
total = 100000
free = 1
time = 0

print "Total number of bottled children is now: ", total
print \

while total > 0:
    x = free
    total = total - x
    time = 100001 - total
    free = time

    print "Total number of bottled children is now: ", total
    print "Total number of children freed is now: ", free
    print "Total amount of time taken is: ", time, "minutes,"
    print time/60,"hours,", time/60/24, "days, or", time/60/24/7, "weeks"
    print \

Results:
Total number of bottled children is now:  -31071
Total number of children freed is now:  131072
Total amount of time taken is:  131072 minutes,
2184 hours, 91 days, or 13 weeks
"""
# this first iteration is okay, but its not taking into consideration that
# 5 kids working at the same time is still one minute

# version 2
"""
total = 100000
free = 1
time = 0

print "Total number of bottled children is now: ", total
print \

while total > 0:
    total = total - free
    time = time + 1
    free = 1 + 100000 - total

    print "Total number of bottled children is now: ", total
    print "Total number of children freed is now: ", free
    print "Total amount of time taken is: ", time, "minutes,"
    print \

Results:
Total number of bottled children is now:  -31071
Total number of children freed is now:  131072
Total amount of time taken is:  17 minutes,
0 hours, 0 days, or 0 weeks
"""
# figured it out, very interesting - this is a direct play off the doubling
# rice for each square on the chess board problem
# one last issue though, we don't want to display negative time

# version 3
total = 100000
free = 1
time = 0

print "Total number of bottled children is now: ", total
print \

while total > 0:
    if total - free > 0:
        total = total - free
        time = time + 1
        free = 1 + 100000 - total
    else:
        free = free + total - 1
        total = 0
        time = time + 1

    print "Total number of bottled children is now: ", total
    print "Total number of children freed is now: ", free
    print "Total amount of time taken is: ", time, "minutes,"
    print \

"""
Results:
Total number of bottled children is now:  0
Total number of children freed is now:  100000
Total amount of time taken is:  17 minutes,
"""
# this version is perfect, no negative sums
