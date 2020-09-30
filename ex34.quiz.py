# my first app

# this is a quiz program which tests a novice programmer's ability to understand
# how indexing works with ordinal (0, 1, 2) and cardinal (1, 2, 3) numbers

# list of animals/answers, and indexes/questions
animal = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
List = [0, 1, 2, 3, 4, 5, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth']

# imports the random interger function
from random import randint

# do not know how this works, imports the text to integer function
import sys
import os
sys.path.append(os.path.abspath("/Users/kevinbai/Exercises/Tools"))
from text_to_int import text2int

# imports the numbers
import numbers

# identifies the global list count as the number of items in the list
# starts problem count at one
list_count = len(List)
problem_count = 1

# opening lines, stylized
print'''
\t Welcome to the Python Index Understanding Quiz (PIUQ)

\t Your list for today: animal
'''

# while loop that comprises the majority of the code to be used
# I could have used a for loop here but that would lower the scalability of the code
# while loop allows me to run this with any list

# this while loop runs up to the point where problem_count = list_count
while problem_count <= list_count:
    # I have a local list_count_updated to keep track
    # of my eliminated, already-asked questions
    list_count_updated = len(List)
    # my random index generator allows me to randomly select the remaining prompts
    number = randint(0, list_count_updated - 1)
    # my list_item variable allows me to use the prompts I randomly generate
    list_item = List[number]

    # prints the list being tested so that the user will always have it for reference
    print "animal = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']"
    # prints the problem count and the current prompt
    print "Problem #%d: What is the animal at %r?" % (problem_count, list_item)

    # asks user for their answers
    user_input = raw_input("> ")

    # if the prompt is a number (which half of them are)
    if isinstance(list_item, numbers.Number) == True:
        # the correct animal can simply be accessed from the list
        correct_animal = animal[list_item]
    # if the prompt is a string(word)
    else:
        # the prompt is coverted into a number
        list_int = text2int(list_item)
        # the number is then used to access the correct animal
        correct_animal = animal[list_int - 1]

    # if the user is correct, print correct
    if user_input == correct_animal:
        print "correct\n"
    # if the user is incorrect, print so and produce the correct answer
    else:
        print "incorrect, the answer is %s\n" % correct_animal

    # removes an element from the prompt list after it is asked to prevent
    # duplicate problems
    List.remove(list_item)

    # augements the problem count by 1
    problem_count += 1
