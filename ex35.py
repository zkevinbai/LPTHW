from sys import exit
from numbers import Number

def gold_room():
    print "This room is full of gold.  How much do you take?"

    choice = raw_input("> ")

    if isinstance(int(choice), Number) == True :
        how_much = int(choice)

    else:
        # when did we define dead? - below
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        # how does this work
        exit(0)

    else:
        dead("You greedy bastard!")

def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    print """\nOptions:
take honey
taunt bear
open door
    """
# while what is true?
# answer: this function runs forever until a break of some kind
    while True:
        choice = raw_input("> ")

        if choice == "take honey":
            dead("The bear looks at you  then slaps your face off.")

        elif choice == "taunt bear" and not bear_moved:
            print "The bear has moved from the door.  You can go through it now."
            bear_moved = True
            return bear_moved

        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")

        elif choice == "open door" and bear_moved:
            gold_room()

        else:
            print "I got no idea what that means."

def cthulu_room():
    print "Here you see the great evil Cthulu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"
    print """\nOptions:
flee
eat head
eat bear
head outside
play poker
    """
    choice = raw_input("> ")

    if "flee" in choice:
        # what is start? - defined later
        start()
    elif "head" in choice:
        dead ("Well that was tasty!")
    else:
        cthulu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which door do you take?"

    choice = raw_input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
