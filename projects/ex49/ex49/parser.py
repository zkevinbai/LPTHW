# makes sense, this pushes out an error if code is not working
class ParserError(Exception):
    pass

# makes sense, Sentence class takes the parts of the sentence and allows you to
# see them one by one
class Sentence(object):
    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.object = obj[1]

def peek(word_list):
    # if you have a nonFalse word list, peek runs and returns the type of
    # the word
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

# do not understand how this helps you use player as a noun
# Now I sort of do, this peek program allows you to check if a word is a certain
# type

def match(word_list, expecting):
    if word_list:
        # NOTICE THE () next to the pop, this removes the first item from the
        # list as opposed to [] which referrs to positions on the list
        word = word_list.pop(0)

        # if word type is what you want, return it
        if word[0] == expecting:
            return word
        else:
            return None

    else:
        return None

def skip(word_list, word_type):
    # uses match to pop off everything of certain type o
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expected a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)
