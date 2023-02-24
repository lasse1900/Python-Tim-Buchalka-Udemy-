import pytz
import datetime

available_choices = ["Europe/Stockholm",
                     "Europe/Helsinki",
                     "Africa/Lusaka",
                     "Europe/Moscow",
                     "Europe/Tallinn",
                     "Africa/Cairo",
                     "America/Edmonton",
                     "Australia/Adelaide",
                     "Europe/Amsterdam"
                     ]

print("\nPlease chooze a timezone to get current time or '0' to quit: \n")

possible_choices = []
for i in range(1, len(available_choices) + 1):
    possible_choices.append(str(i) + ": " + available_choices[i-1])
print(possible_choices)

valid_choices = []
for i in range(1, len(available_choices) + 1):
    valid_choices.append(str(i))

current_choice = "-"

while current_choice != "0":
    if current_choice in valid_choices:
        index = int(current_choice) - 1
        country = available_choices[index]
        print(country)
        tz_to_display = pytz.timezone(country)
        local_time = datetime.datetime.now(tz=tz_to_display)
        print(f"The time in {country} is {local_time}")
        print("UTC is {}".format(datetime.datetime.utcnow()))

    current_choice = input()

