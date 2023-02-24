# https://docs.python.org/3/library/stdtypes.html#string-methods

'''
def is_palindrome_sentence1(sentence: str) -> bool:
    alpha_sentence = [""]
    string_alpha = ""
    for index in range(len(sentence)):
        if sentence[index].isalpha():
            alpha_sentence.append(sentence[index])
    string_alpha.join(alpha_sentence)
#   string_alpha = ''.join(map(str, alpha_sentence))
    string_alpha = ''.join(alpha_sentence)
    return string_alpha[::-1].casefold() == string_alpha.casefold()
'''


def is_palindrome_sentence(sentence: str) -> bool:
    string = ""
    for char in sentence:
        if char.isalnum():
            string += char
    return string[::-1].casefold() == string.casefold()


sentence = input("Give a sentence to test weather a palindrome: ")
# sentence = "Do gees see god?"

if is_palindrome_sentence(sentence):
    print(f"'{sentence}' is a palindrome")
else:
    print(f"'{sentence}'' is not a palindrome")


p = is_palindrome_sentence('racecar')
print(p)