def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers
    :param x: first number to multiply
    :param y: second number to multiply
    :return: the return of multiplication of numbers a and b
    """
    result = x * y
    return result


answer = multiply(12, 5)
print(answer)

for val in range(1, 5):
    two_times = multiply(2, val)
    print(two_times)
