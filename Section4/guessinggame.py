answer = 5

print("Please quess a number between 1 and 10: ")
guess = int(input())

if guess < answer:
    print("Please quess higher")
    quess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed corretly")
elif guess > answer:
    print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed corretly")
else:
    print("You got it first time")
