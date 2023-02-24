panagram = """The quick brown
fox jumps\t
over the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))


# values = "".join(char if char not in separators else " " for char in numbers).split()
generated_list = ['9',' ',
                  '2','2','3',' ',
                  '3','7','2',' ',
                  '0','3','6',' ',
                  '8','5','4',' ',
                  '7','7','5',' ',
                  '8','0','7']
values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

print('-'*30)

# Use a loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints.

# replace the values in place
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print(values_list)


# create a new list
integer_values = []
for value in values_list:
    integer_values.append(int(value))
print(integer_values)

print('-'*30)
list_of_ints = [1,7,11,13,15,17,22,31]
str_of_ints = [str(int) for int in list_of_ints]
print(str_of_ints)

vals = " : ".join(str_of_ints)
print(vals)


