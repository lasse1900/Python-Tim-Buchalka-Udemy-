# https://www.udemy.com/course/python-the-complete-python-developer-course/learn/quiz/5081438#questions


def sum_eo(n,t):
    """
    Sum of a given range of numbers, even or odd
    :param n: number of the range, how many numbers starting from zero
    :param t: parameter telling e=even, o = odd whether counting even or odd sum
    :return: the sum of rnge of numbers
    """
    list = []
    if t == 'e':
        for i in range(1,n):
            if i % 2 == 0:
                list.append(i)
        return sum(list)
    elif t == 'o':
        for i in range(1,n):
            if i % 2 != 0:
                list.append(i)
        return sum(list)
    else:
        return -1


print(sum_eo(10,'e'))


def sum_eo_Tim(n, t):
    """Sum even or odd numbers in range.

    Return the sum of even or odd natural numbers, in the range 1..n-1.

    :param n: The endpoint of the range. The numbers from 1 to n-1 will be summed.
    :param t: 'e' to sum even numbers, 'o' to sum odd numbers.
    :return: The sum of the even or odd numbers in the range.
            Returns -1 if `t` is not 'e' or 'o'.
    """
    if t == "e":
        start = 2
    elif t == 'o':
        start = 1
    else:
        return -1

    return sum(range(start, n, 2))


x = sum_eo_Tim(10, 'e')
print(x)
