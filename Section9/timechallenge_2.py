import pytz
import datetime

available_zones = {"1": "Europe/Stockholm",
                     "2": "Europe/Helsinki",
                     "3": "Africa/Lusaka",
                     "4": "Europe/Moscow",
                     "5": "Europe/Tallinn",
                     "6": "Africa/Cairo",
                     "7": "America/Edmonton",
                     "8": "Australia/Adelaide",
                     "9": "Europe/Amsterdam"
                   }


print("\nPlease chooze a timezone to get current time or '0' to quit: \n")

for place in sorted(available_zones):
    print(f"\t {place}. {available_zones[place]}")

while True:
    choice = input()

    if choice == "0":
        break

    if choice in available_zones.keys():
        tz_to_display = pytz.timezone(available_zones[choice])
        world_time = datetime.datetime.now(tz=tz_to_display)
        print("The time in {} is {} {}".format(available_zones[choice], world_time.strftime('%A %x %X %z'),world_time.tzname()))
        print("Local time is {}".format(datetime.datetime.now().strftime('%A %x %X')))
        print("UTC time is {}".format(datetime.datetime.utcnow().strftime('%A %x %X')))

