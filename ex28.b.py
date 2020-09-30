print "\nExercise 28 - Boolean Practice - Logic Quiz\n"

number = 0
prompt = "True and True"
prompt_value = True and True

def problem_tester(number, prompt, prompt_value):
    number += 1
    # prompt_string = str(prompt)

    # I need to find a way to have prompt string return the literal phrasing of
    # prompt and not the returned value of prompt
    # The problem is that python automatically knows that True and True
    # evaluates out to true, so even if I use str(), I will only be able to make
    # a "True" or "False" string and not the phrasing

    print "Problem number %d: %s?" % (number, prompt)

    answer = prompt_value

    user_answer = raw_input("True or False? ")

    if user_answer == str(answer):
        print "correct"
    else:
        print "incorrect"

problem_tester(number, prompt, prompt_value)
