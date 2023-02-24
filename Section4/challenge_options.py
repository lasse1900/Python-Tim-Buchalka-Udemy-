print("Please choose your option from the list below: ")
print("1.\tLearn Python")
print("2.\tLearn Java")
print("3.\tGo swimming")
print("4.\tHave dinner")
print("5.\tGo to bed")
print("6.\tExit")


choices = [1,2,3,4,5,6]
choice = 1

while choice in choices:
    choice = int(input("Please enter your choice: "))
    print(f"Your choice was: {choice}")
    if choice == 6:
        print("You choze to exit")
        break

