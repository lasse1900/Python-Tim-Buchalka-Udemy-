available_parts = {"1":"computer",
                   "2":"monitor",
                   "3":"keyboard",
                   "4":"mouse",
                   "5":"hdmi cable",
                   "6":"dvd drive",
                   }

computer_parts = [] # create an empty list
current_choice = None

while current_choice != '0':
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print(f"Adding {chosen_part}")
            computer_parts.append((chosen_part))
        print(f"Your list now contains: {computer_parts}")
    else:
        print("Please add options from the list below:")
        for key, value in available_parts.items():
            print(key, value, sep=": ")
        print("0: to finnish")

    current_choice = input("> ")

