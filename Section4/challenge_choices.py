choice = " "
while choice != "0":
    if choice in "123456":
        print("Your choice {}".format(choice))
    else:
        print("Please choose your otion from the list below: ")
        print("1.\tLearn Python")
        print("2.\tLearn Java")
        print("3.\tGo swimming")
        print("4.\tHave dinner")
        print("5.\tGo to sleep")
        print("0.\tExit")
    choice = input()