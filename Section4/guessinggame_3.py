import random

highest = 1000
answer = random.randint(1,highest)
print(answer) # TODO: Remove after testing
guess = ""
number_of_guesses = 1
print("Please quess a number between 1 and {}: ".format(highest))

while guess != answer:

    guess = int(input())
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


