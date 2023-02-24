def sum_numbers(*num: float) -> float:
    """
    Count the sum of numbers
    :param num: `integer/float`
    :return: sum of numbers
    """
    sum = 0

    for n in num:
        sum = sum + n

    return sum


print(sum_numbers(12.5,3.147,98.1))
