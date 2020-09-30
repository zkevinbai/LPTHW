people = 30
cars = 40
trucks = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
# else clause only comes into effect when cars = people
else:
    print "We can't decide."

if trucks > cars:
    print "That's too many trucks."
elif trucks < cars:
    print "Maybe we could take the trucks."
# else clause only comes into effect when trucks = cars
else:
    print "We still can't decide."

if people > trucks:
    print "Alright, let's just take the trucks."
# else clause comes into effect when people <= trucks
else:
    print "Fine, let's stay home then."


# challenge time, lets simplify this down to one block
# this code basically says to take trucks if there are more trucks than cars
# or to take cars if there are more cars than people
'''
if trucks >= people or trucks < cars:
    print "We should take the trucks."
elif cars >= people or  trucks > cars:
    print "We should take the cars."
else:
    print "Fine, let's stay home then."
'''
