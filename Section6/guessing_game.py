import random


def get_integer(promt):
    """
    Get an integer from Standard Input (stdin).

    The function will continue looping, and prompting
    the user, until a valid `int` is entered.

    :param promt: The string that the user will see, when
        they're promted to enter the value.
    :return: The integer that the user enters.
    """
    while True:
        temp = input(promt)
        if temp.isnumeric():
            return int(temp)
        else:
            print("Please give a valid numeric input!")

help(get_integer)

'''
print(input.__doc__)
print("*" * 80)
print(get_integer.__doc__)
print("*" * 80)
'''

highest = 1000
answer = random.randint(1,highest)
print(answer) # TODO: Remove after testing
guess = ""
number_of_guesses = 1
print("Please quess a number between 1 and {}: ".format(highest))

while guess != answer:
    guess = get_integer(": ")
    if guess == 0:
        break
    if guess == answer:
        print("You got it first time")
        break
    else:
        if guess < answer:
            print("Please guess higher")
        else:
            print("Please guess lower")
    number_of_guesses += 1
print("Number of guesses {} ".format(number_of_guesses))


