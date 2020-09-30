# assigns the variable formatter to mean a string of four formats
formatter = "%r %r %r %r"

# calls the variable formatter to print a certain output
print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)
# alternate print formatter % ('I had this thing,', 'That you could type up right.', 'But it didnt sing.', 'So I said goodnight.')


# Notice that the last line of output uses both single-quotes and double-quotes
# for individual pieces. Why do you think that is?
# This is because formatter is already formatted to have a string-type output
