# instructions, find the animal
'''
animal = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

print "The animal at 1."
print animal[1] + '\n'

print "The third (3rd) animal."
print animal[2] + '\n'

print "The first (1st) animal."
print animal[0] + '\n'

print "The animal at 3."
print animal[3] + '\n'

print "The fifth (5th) animal."
print animal[4] + '\n'

print "The animal at 2."
print animal[2] + '\n'

print "The sixth (6th) animal."
print animal[5] + '\n'

print "The animal at 4."
print animal[4] + '\n'
'''
# lets make a quiz
animal = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']
List = [0, 1, 2, 3, 4, 5, 'first', 'second', 'third', 'fourth', 'fifth', 'sixth']

# got from http://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9
from random import randint

# dont know enough to make this or even how to import it
# text2int is from http://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
# import method is from http://stackoverflow.com/questions/2349991/python-how-to-import-other-python-files
import sys
import os
sys.path.append(os.path.abspath("/Users/kevinbai/Exercises/Tools"))
from text_to_int import text2int

import numbers

list_count = len(List)
problem_count = 1

print'''
\t Welcome to the Python Index Understanding Quiz (PIUQ)

\t Your list for today: animal
'''

while problem_count <= list_count:
    list_count_updated = len(List)
    number = randint(0, list_count_updated - 1)
    list_item = List[number]

    print "animal = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']"
    print "Problem #%d: What is the animal at %r?" % (problem_count, list_item)

    user_input = raw_input("> ")

# dont know what this below is, came from (http://stackoverflow.com/questions/4187185/how-can-i-check-if-my-python-object-is-a-number)
    if isinstance(list_item, numbers.Number) == True:
        correct_animal = animal[list_item]
    else:
        list_int = text2int(list_item)
        correct_animal = animal[list_int - 1]

    if user_input == correct_animal:
        print "correct\n"
    else:
        print "incorrect, the answer is %s\n" % correct_animal

    List.remove(list_item)

    problem_count += 1

# problems faced
# cannot ask user questions
# cannot correct the user answers
    # cannot identify what is an integer or string from my list which has both
    # cannot convert strings to numbers
    # cannot import my functions
# cannot randomize the questions
# cannot ask each question only once

# all problems now solved
# 8:30 - 11:00 or 2 hours 30 minutes to make this

# not perfect, many functionalities left to go but perfect for my needs
# could add a way to tell someone their grade
# could fix the text2int function, I had to maul it a little and it can no longer be used generally
# this is my first real program
