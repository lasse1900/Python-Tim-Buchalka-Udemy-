# number = "9,223;372:036 854,775;807"
number = input("Please enter a series of numbers, using any separators you like: ")
separators = ""
# separators = number[1::4]

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])


total = sum([int(val) for val in values])
print(f"Total: {total}")