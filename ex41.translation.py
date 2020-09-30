# from computer import random, sys
# from urllib import urlopen
import random
from urllib import urlopen
import sys

# define WORD_URL as the http link
WORD_URL = "http://learncodethehardway.org/words.txt"
# create the empty list WORDS
WORDS = []

# create the phrases dictionary with all of the posibilities for object oriented
# questions that I could have
# i'm guessing that %%%, *** and @@@ have no meaning
PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __init__(self, ***)" :
        "class %%% has-a __init__ that takes self and *** parameters.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function named *** that takes self and @@@ parameters.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, and call it with parameters self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

#- do they want to drill phrases first
# if the input from the commandline is 2 items and the second cardinal (position 1)
# item is the string "English", set the PHRASE_FIRST variable to True
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

#- load up the words from the website
# uses a for loop to append every word from the url to the empty list WORDS
for word in urlopen(WORD_URL).readlines():
    WORDS.append(word.strip())

# create the convert function with the snippet and phrase parameters
def convert(snippet, phrase):
    # we need to understand this Russian nesting doll from the inside out
    # 1 snippet.count("%%%") counts how many instances of %%% appears inside snippet
    # 2 random.sample(WORDS, snippet.count("%%%"))] identifies the population as
    # WORDS and the k as the snippet.count("%%%") result and returns a list of k
    # length of unique items from the population
    # 3 w.capitalize capitalizes the firs letter of the string w
    # for each object in the snippet.count list list
    class_names = [w.capitalize() for w in
                    random.sample(WORDS, snippet.count("%%%"))]
    # same as above, other names is a list of snippet.count("***") length from the
    # WORDS list population of randomly selected non repeating terms
    other_names = random.sample(WORDS, snippet.count("***"))
    # creates the empty lists results and param_names
    results = []
    param_names = []

    #for each term in the range 0 to the snippet.count("@@@"), set param_count as a
    # random interger between 1 and 3 inclusive
    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        # add to the empty list param_names a joined string of the lists WORDS and
        # param_count with ', ' as the separator
        param_names.append(', '.join(random.sample(WORDS, param_count)))

    # for sentence in the snippet and phrase lists, copy each sentence
    #- for each sentence in snippet
    for sentence in snippet, phrase:
        result = sentence[:]

        # for each word in class_names list, each "%%%" in result is replaced with
        # that word with a maximum instance of once
        #- fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)

        # for each word in other_names list, each "***" in result is replaced with
        # that word with a maximum instance of once
        #- fake other names
        for word in other_names:
            result = result.replace("***", word, 1)

        # for each word in param_names list, each "@@@" in result is replaced with
        # that word with a maximum instance of once
        #- fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)

        # append the result to the results list
        results.append(result)

    # return the results list
    return results


#- keep going until they hit CTRL-D
# error testing
try:
    # while True, snippets list is set to the all of the keys() from the PHRASES dictionary
    while True:
        snippets = PHRASES.keys()
        #randomizes the list snippets
        random.shuffle(snippets)

        # for each item in the snippets list
        for snippet in snippets:
            # phrase is set as the values matching the keys snippet from the PHRASES dictionary
            phrase = PHRASES[snippet]
            # the question and answer is set equal to the returned results of the
            # convert function with parameters snippet and phrase lists
            question, answer = convert(snippet, phrase)
            # if PHRASE_FIRST evaluates to true
            if PHRASE_FIRST:
                # question is the answer and answer is the question
                # implied that otherwise answer = answer and question = question
                question, answer = answer, question

            # print question
            print question

            # prompt
            raw_input("> ")
            # prints the answer
            print "ANSWER:  %s\n\n" % answer

except EOFError:
    # except in the case where the function hits the end of file without reading data 
    print "\nBye"
