ten_things = "Apples Oranges Crows Telephones Light Sugar"

print "\nWait there are not 10 things in that list. Let's fix that."

stuff = ten_things.split(' ') # what is split? separates all things in ten_things
# into a list

more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # what is this version of pop? removes the last item
    # from more_stuff and removes it from more_stuff

    print "Adding: ", next_one
    stuff.append(next_one)
    print "There are %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print "1", stuff, "\n"

print stuff[-1] # returns the term before 0 or the last term
print "2", stuff, "\n"

print stuff.pop()
    # pop? removes the last item from stuff and returns it
print "3", stuff, "\n"

print ''.join(stuff) # join? join takes the string to the left and uses it as glue to
# join the objects of the list (in this case stuff)
print "4", stuff, "\n"

print '#'.join(stuff[3:5])
print "5", stuff, "\n"

# all good, got it 
