# my first game

from sys import exit

print "\n\t Welcome to the Riddle Dungeon, you must play if you want to leave.\n"

# enter rooms function, thank you tuples!!!
def enter_room(choice):
    if "starting" in choice:
        starting_room()

    elif choice in ("north", "North"):
        North_room()

    elif choice in ("south", "South"):
        South_room()

    elif choice in ("east", "East"):
        East_room()

    elif choice in ("west", "West"):
        West_room()

    else:
        print "That is not a room."
        print "Which room do you want to go to?"
        choice = raw_input("> ")
        enter_room(choice)

# if dead function
def dead(why):
    print why, "\nTry again!"
    exit(0)

# # Rooms
# North Room Giant
North_room_status = "unsolved"
def North_room():
    global North_room_status
    global riddles_solved

    if North_room_status == "unsolved":
        print '''\nThe door dissapears behind you.'''
        print '''\nYou are in a frozen wasteland and see a towering giant in front
        \rof you.  \"ANSWER MY RIDDLE OR BE BROKEN IN TWO!\" he bellows.\n'''
        print '''What becomes invisible when held still, but when grasped in your
        \rhands is reduced to nil?'''

        answer = raw_input("> ")

        if answer in ("ice", "Ice"):
            print "\n\"Well done human, you have beaten the North Room and may proceed.\"\n"

            riddles_solved += 1
            riddles_remaining = 5 - riddles_solved
            North_room_status = "solved"

            print "You have solved %d riddles, %d more remain.\n" % (riddles_solved, riddles_remaining)
            print "You are transported back to the starting room.\n"
            enter_room("starting")

        else:
            print "\n\"Wrong!\""
            dead("The giant grabs you and breaks you in two.")

    else:
        print "\nYou have already beaten the North room, try another.\n"
        enter_room("starting")

# South Room Wizard
South_room_status = "unsolved"
def South_room():
    global South_room_status
    global riddles_solved

    if South_room_status == "unsolved":
        print '''\nThe door dissapears behind you.'''
        print '''\nYou are in a enormous library and see a ancient wizard in front of you.
        \r\"Answer my riddle or be electrocuted where you stand.\" he states.\n'''
        print '''I'm light as a feather, yet the strongest man can't hold me for
        \rmore than 5 minutes. What am I?'''

        answer = raw_input("> ")

        if answer in ("breath", "air"):
            print "\n\"Well done human, you have beaten the South Room and may proceed.\"\n"

            riddles_solved += 1
            riddles_remaining = 5 - riddles_solved
            South_room_status = "solved"

            print "You have solved %d riddles, %d more remain.\n" % (riddles_solved, riddles_remaining)
            print "You are transported back to the starting room.\n"
            enter_room("starting")

        else:
            print "\n\"Incorrect.\""
            dead("The wizard arcs a bolt of lighting from his staff and electrocutes you.")

    else:
        print "\nYou have already beaten the South room, try another.\n"
        enter_room("starting")

# East Room Dragon
East_room_status = "unsolved"
def East_room():
    global East_room_status
    global riddles_solved

    if East_room_status == "unsolved":
        print '''\nThe door dissapears behind you.'''
        print '''\nYou are in an flaming volcano and see a fearsome dragon in front of you.
        \r\"ANSWER MY RIDDLE OR BE REDUCED TO ASHES!\" he roars.\n'''
        print '''I am an instrument that you can hear, but you can not touch or see me.
        \rWhat am I?'''

        answer = raw_input("> ")

        if answer in ("voice", "layrynx"):
            print "\n\"Well done human, you have beaten the East Room and may proceed.\"\n"

            riddles_solved += 1
            riddles_remaining = 5 - riddles_solved
            East_room_status = "solved"

            print "You have solved %d riddles, %d more remain.\n" % (riddles_solved, riddles_remaining)
            print "You are transported back to the starting room.\n"
            enter_room("starting")

        else:
            print "\n\"Wrong!\""
            dead("The dragon opens his jaws and burns you to ashes.")

    else:
        print "\nYou have already beaten the East room, try another.\n"
        enter_room("starting")

# West Room Knight
West_room_status = "unsolved"
def West_room():
    global West_room_status
    global riddles_solved

    if West_room_status == "unsolved":
        print '''\nThe door dissapears behind you.'''
        print '''\nYou are in a stunning castle and see a powerful knight in front of you.
        \r\"Answer my riddle or be cut down where you stand.\" he states.\n'''
        print '''What loses its head in the morning and gets it back at night?'''

        answer = raw_input("> ")

        if answer in ("pillow", "Pillow"):
            print "\n\"Well done human, you have beaten the West Room and may proceed.\"\n"

            riddles_solved += 1
            riddles_remaining = 5 - riddles_solved
            West_room_status = "solved"

            print "You have solved %d riddles, %d more remain.\n" % (riddles_solved, riddles_remaining)
            print "You are transported back to the starting room.\n"
            enter_room("starting")

        else:
            print "\n\"Wrong.\""
            dead("The knight swings his sword and cuts you in half.")

    else:
        print "\nYou have already beaten the West room, try another.\n"
        enter_room("starting")

# Starting Room Sphinx
riddles_solved = 0
def starting_room():
    # starting room standard
    if riddles_solved == 0:
        print '''You are in the starting room, it has four doors, one to the
        \rNorth, one to the South,one to the East and one to the West.\n'''

        print "You can look around or go through a door.\n"

        print "What do you want to do?"
        not_playing = True

        while not_playing:
            reply = raw_input("> ")

            if "look around" in reply:
                print """You see a message carved in stone, You read a message
                \ron the wall, 4 guardians protect each room.  
                \rAnswer their riddles or face your doom.\n"""

            elif "door" in reply:
                not_playing = False

            else:
                print "That is not an option.\n"

        print "\nWhich way do you want to go?"

        choice = raw_input("> ")
        enter_room(choice)

    elif riddles_solved < 4:
        print '''You are in the starting room, it has four doors, one to the
        \rNorth, one to the South,one to the East and one to the West.'''

        print "\nWhich way do you want to go?"

        choice = raw_input("> ")
        enter_room(choice)

    # if NSEW rooms beaten
    else:
        print '''The room is now transformed into a dessert and a majestic sphinx,
        \rstands in front of you.  It proceeds to speak:\n'''

        print '''\"You have beaten the four guardians of the Riddle Dungeon.
        \rNow you must face me!\"\n'''

        print '''\"If you answer my riddle I will permit you to leave, but if you
        \rfail I will obliterate you.\"\n'''

        print '''I have a magnet but I do not stick to metal
        \rI have a needle but I can not sew
        \rI can have scales but I will not weigh anything
        \rI help you find your way but I am no map
        \rI have NEWS on me but I am not a television
        \rYou have been inside me this whole time
        \rWhat am I?'''

        answer = raw_input("> ")

        if "compass" in answer:
            print """\nCongratulations! you have beaten all five guardians of
            \r the Riddle Dungeon, you are magically transported home."""
            exit(0)
        else:
            print "\n\"Wrong!\""
            dead("The sphinx's eyes light up with power and obliterate you.")

starting_room()
