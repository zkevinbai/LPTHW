# defines the function cheese_and_crackers which takes two arguments and
# prints out how many there are of each
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "Man that is enough for a party!"
    print "Get a blanket.\n"

user_cheese = int(raw_input("How many cheeses do you have right now?"))
user_crackers = int(raw_input("How about boxes of crackers?"))

cheese_and_crackers(user_cheese, user_crackers)

# plugs in the arguments 20 and 30 into the cheese_and_crackers function
print "We can just give the function numbers diectly:"
cheese_and_crackers(20,30)

# makes variables
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# plugs in the made variables
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# plugs in numbers which require math
print "We can even do math inside:"
cheese_and_crackers(10 + 20, 5 + 6)

# combines variables and math
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
