# to make my quiz app on ex 34, I had to modify this code (one to first) to better fit my quiz
# this will no longer work for numbers one through six due to my changes
def text2int(textnum, numwords={}):
    if not numwords:
      units = [
        "zero", "first", "second", "third", "fourth", "fifth", "sixth", "seven", "eight",
        "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
        "sixteen", "seventeen", "eighteen", "nineteen",
      ]

      tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

      scales = ["hundred", "thousand", "million", "billion", "trillion"]

      numwords["and"] = (1, 0)
      for idx, word in enumerate(units):    numwords[word] = (1, idx)
      for idx, word in enumerate(tens):     numwords[word] = (1, idx * 10)
      for idx, word in enumerate(scales):   numwords[word] = (10 ** (idx * 3 or 2), 0)

    current = result = 0
    for word in textnum.split():
        if word not in numwords:
          raise Exception("Illegal word: " + word)

        scale, increment = numwords[word]
        current = current * scale + increment
        if scale > 100:
            result += current
            current = 0

    return result + current

# print text2int("seven billion one hundred million thirty one thousand three hundred thirty seven")
# 7100031337

# I don't understand most of this at the moment, this is something i pulled from
# http://stackoverflow.com/questions/493174/is-there-a-way-to-convert-number-words-to-integers
