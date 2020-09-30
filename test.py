
Write a program that prints the numbers from 1 to 100.
But for multiples of three print "Fizz" instead of the number
and for the multiples of five print "Buzz".
For numbers which are multiples of both three and five print "FizzBuzz".

x = 0

def fizzbuzz():
    global x
    while x< 100:
        x += 1
        if x % 15 == 0 :
            print "FizzBuzz"
        elif x % 3 == 0:
            print "Fizz"
        elif x % 5 == 0:
            print "Buzz"
        else:
            print x

fizzbuzz()
