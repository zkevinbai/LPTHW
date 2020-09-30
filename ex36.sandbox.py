# 


# maybe enter room and run room would be fun

# new thought, connecting rooms with numbers directly

def enter_room(choice):
    if "starting" in choice:
        starting_room()

    elif choice == "South" or "south":
        South_room()

    elif choice == "East" or "east":
        East_room()

    elif choice == "West" or "west":
        West_room()

    else:
        print "That is not a room."
        print "Which room do you want to go to?"
        choice = raw_input("> ")
        enter_room(choice)

choice = raw_input()
enter_room(choice)

def dead(why):
    print why, "Try again!"
    exit(0)

North_room_status = "unsolved"

def North_room():
    global North_room_status
    if North_room_status == "unsolved":
        print '''\nYou are in a frozen wasteland and see a towering giant in front
of you.  \"ANSWER MY RIDDLE OR BE BROKEN IN TWO! He bellows.\"\n'''
        print '''What becomes invisible when held still, but when grasped in your
hands is reduced to nil?'''
        answer = raw_input("> ")

        if "ice" in answer:
            print "\nWell done human, you have beaten the North Room and may proceed."
            riddles_solved += 1
            North_room_status = "solved"
            enter_room(starting)

        else:
            print "Wrong!"
            dead("The giant grabs you and snaps you in two.")

    else:
        print "You have already beaten this room, try another."
        enter_room(starting)

riddles_solved = 0

def starting_room():
    # starting room standard
    if riddles_solved != 4:
        print '''You are in the starting room, it has four doors, one to the
North, one to the South,one to the East and one to the West.\n'''

        print "You can look around or go through a door.\n"

        print "What do you want to do?"
        not_playing = True

        while not_playing:
            reply = raw_input("> ")

            if "look around" in reply:
                print """You read a message on the wall, 4 guardians protect each room.
answer their riddles or face your doom.\n"""

            elif "door" in reply:
                not_playing = False

            else:
                print "That is not an option.\n"

        print "\nWhich way do you want to go?"
        choice = raw_input("> ")

        enter_room(choice)
    # if NSEW rooms beaten
    else:
        print '''The room is now transformed into a dessert and a majestic sphinx,
    stands in front of you.  It proceeds to speak:\n'''
        print '''You have beaten the four guardians of the Riddle Dungeon.
Now you must face me!\n'''
        print '''If you answer my riddle I will permit you to leave, but if you
fail I will eat you whole.\n'''
        print '''I have a magnet but I do not stick to metal
I have a needle but I can not sew
I can have scales but I will not weigh anything
I help you find your way but I am no map
I have NEWS on me but I am not a television
You have been inside me this whole time
What am I?'''

        answer = raw_input("> ")

        if "compass" in answer:
            print "Congratulations! you have beaten the Riddle Dungeon."
            exit(0)
        else:
            print "Wrong!"
            dead("The Sphinx pounces and eats you whole.")


rooms = ["starting", "North", "South", "East", "West"]
status = ["finished", "unfinished"]
guardians = ["majestic Sphinx", "towering Giant", "ancient Wizard", "fearsome Dragon",
"powerful Knight"]


# alternate room entrance mechanism


def enter_room(room):
    room_num = "undefined"

    while room_num != int
        if room == "North":
            room_num = 1
        elif room == "South":
            room_num = 2
        elif room == "East":
            room_num = 3
        elif room == "West":
            room_num = 4
        else:
            print "That is not a room."
            choice = raw_input("Which room do you want to go to? ")

    print "You are now at the rooms[room_num] room, a guardians[room_num] stands before you.

    print riddle[room_num]
