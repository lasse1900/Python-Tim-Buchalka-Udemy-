'''
# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Your code goes here ...
for char in text.casefold():
    # We're only counting letters and digits (no punctuation).
    if char.isalnum():
        word_count[char] = word_count.setdefault(char, 0) + 1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)

'''

# We need an empty dictionary, to store and display the letter frequencies.
word_count = {}

# Text string
text = "Later in the course, you'll see how to use the collections Counter class."

# Iterate over every character in the string.
for char in text.casefold():
    # We're only counting letters and digits (no punctuation).
    if char.isalnum():
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1

# Printing the dictionary
for letter, count in sorted(word_count.items()):
    print(letter, count)
