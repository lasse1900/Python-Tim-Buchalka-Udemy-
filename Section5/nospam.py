menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg", "spam"],
    ["egg", "bacon", "spam"],
    ["egg", "bacon", "sausage", "spam"],
    ["spam", "bacon", "sausage", "spam"],
    ["spam", "sausage", "spam", "bacon", "spam", "tomato", "spam"],
    ["spam", "egg", "spam", "spam", "bacon", "spam"],
]

'''
for meal in menu:
    if "spam" not in meal:
        print()
    elif "spam" in meal:
        meal.remove("spam")
        print()

    for item in meal:
        print(item, end=" ")
'''


# First workin example
for meal in menu:
    for index in range(len(meal) -1, -1, -1):
        if meal[index] == "spam":
            del meal[index]

    print(meal)

print('-'*30)

# Second workin example

for meal in menu:
    for item in meal:
        if item != "spam":
            print(item,end=" ")
    print()

print('-'*30)

for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)