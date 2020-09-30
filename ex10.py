"I am 6'2\" tall." # escape double-quote inside string
'I am 6\'2" tall.' # escape single-quote inside string

# defines tabby_cat variable as a string with a tab escape that comes first
# this basically just means to excecute the escape action when printing or
# acting on the string
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm slit\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

print 'hi I\'m fred'

print 'hi I\'m fred'

tab = "\t"
print "%sto the left is a tab" % tab


# while True:
#    for i in ["/","-","|","\\","|"]:
#        print "%s\r" % i,
