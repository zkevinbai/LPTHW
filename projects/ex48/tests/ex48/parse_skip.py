
from lexicon import scan

user_input =  scan("the bear run south")

def parse_skip():

    user_input[:] = [item for item in user_input if 'stop' not in item]
    user_input[:] = [item for item in user_input if 'ERROR' not in item]

    print"Finished\n"
    print user_input
    print"+++\n"
