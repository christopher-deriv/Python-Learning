# triple """ lets you use multiple lines in a string

text = """

a b c a a b
"""

print(text.split())

word_count = {}

for word in text.split():
    # if is checking if the first response in the dictionary is already there if it is then add one
    if word in word_count:
        word_count[word] += 1
    # if it's not then go to else and set it to 1
    else:
        word_count[word] = 1

print (word_count)