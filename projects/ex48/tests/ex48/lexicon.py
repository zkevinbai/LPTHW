
dictionary = [
              ('direction', 'north', 'south', 'east', 'west', 'up', 'down'
              'left', 'right', 'back'),
              ('verb', 'open', 'go', 'run', ' stop', 'kill', 'eat'),
              ('stop', 'the', 'in', 'of', 'from', 'at', 'it'),
              ('noun', 'door', 'bear', 'princess', 'cabinet'),
              ('number', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
              ]

def scan(sentence):
    # manual entry

    words = sentence.split()
    result = []

    for i in words:
        if i in dictionary[0]:
            result.append(('direction', i))
        elif i in dictionary [1]:
            result.append(('verb', i))
        elif i in dictionary [2]:
            result.append(('stop', i))
        elif i in dictionary [3]:
            result.append(('noun', i))
        else:
             try:
                 cat = int(i)
                 result.append(('number', cat))
             except ValueError:
                 result.append(('ERROR', i))

        #number handling singles
#        elif i in dictionary [4]:
#            cat = int(i)
#            result.append(('number', cat))
#        else:
#            result.append(('ERROR', i))
    return result
    print result

"""
first_word = ('verb', 'go')
second_word = ('direction', 'north')
third_word = ('direction', 'west')
sentence = [first_word, second_word, third_word]

This is just an example, but that's basically the end result.
You want to take raw input from the user, carve it into words with split,
analyze those words to identify their type, and finally make a sentence.
"""
