# Now to write the main script

from random import randint
from ex45b import is_dead
from sys import exit

progress_list = [1, 1, 1,]

class ThreeCardMonte(object):
    def game_on(self):

        global progress_list
        guesses = 0
        right_card = str(randint(1,3))

        while guesses < 2:
            user_input = raw_input("Which is the right card, 1, 2 or 3? ")
            if user_input != right_card:
                print "incorrect!"
                guesses += 1
                print right_card
                if guesses == 2:
                    progress_list.append(1)
                else:
                    pass

            else:
                print "correct!"
                progress_list.remove(1)
                break

            is_dead()

class FirstRoom(ThreeCardMonte):
    def game_on(self):
        print "\nWelcome to the First Room"
        print """\nThere are three cards in front of you and only one is correct,
            \rfind the right card and you can advance.\n"""
        super (FirstRoom, self).game_on()
        if len(progress_list) == 2:
            next_room = SecondRoom()
            next_room.game_on()
        else:
            exit(1)

class SecondRoom(ThreeCardMonte):
    def game_on(self):
        print "\nWelcome to the Second Room"
        print """\nThere are three cards in front of you and only one is correct,
            \rfind the right card and you can advance.  Fail and you'll be sent
            \rback a room.\n"""
        super (SecondRoom, self).game_on()
        if len(progress_list) == 1:
            next_room = ThirdRoom()
            next_room.game_on()
        else:
            next_room = FirstRoom()
            next_room.game_on()

class ThirdRoom(ThreeCardMonte):
    def game_on(self):
        print "\nWelcome to the Third Room"
        print """\nThere are three cards in front of you and only one is correct,
            \rfind the right card and you can advance.  Fail and you'll be sent
            \rback to the second room.\n"""
        super (ThirdRoom, self).game_on()
        if len(progress_list) == 0:
            print "\nConratulations! You've finished this highly pointless game!\n"
        else:
            next_room = SecondRoom()
            next_room.game_on()

next_room = FirstRoom()
next_room.game_on()
