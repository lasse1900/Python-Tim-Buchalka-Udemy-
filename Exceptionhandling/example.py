def factorial(n):
    # n! can also be defined as n * (n-1)!
    """ calculates n! recursively """
    if n < 1:
        return 1
    else:
        # print(n / 0)
        return n * factorial(n-1)

try:
    print(factorial(900))
except (RecursionError, OverflowError):
    print("This program doesn't calculate factorials that large!")
# except ZeroDivisionError:
#     print("Zero division error!")

print("Program terminating")