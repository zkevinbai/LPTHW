# This will be the random number generator

from random import randint

def is_dead():
    dead_list = [
    "Sorry, try again.",
    "Not good enough.",
    "Oh brother.",
    "In your dreams.",
    ]

    death_quip = dead_list[randint(1, len(dead_list)-1)]

    print "\n" + death_quip + "\n"
