added_numbers = input("Give three (3) integrs separated with comma (,): ")

number_list = added_numbers.split(",")

# print(number_list)

total_sum = 0
for index, integer in enumerate(number_list):
    if index == 0 or index == 1:
        total_sum += int(integer)
    elif index == 2:
        total_sum -= int(integer)

print(total_sum)