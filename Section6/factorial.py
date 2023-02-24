

def factorial(n: int) -> int:
    """
    Counts the `factorial` up to given number
    :param n: given `integer` to limit where to stop counting
    :return: `None`
    """
    fact = 1
    print(0,1)
    for i in range(1, n):
        print(i, end=" ")
        fact = fact * i
        print(fact)
    return fact

factorial(36)


'''
def factorial(n: int) -> int:
    """Return factorial"""
    if n <= 1:
        return 1
    result = 2
     
    for x in range(3, n + 1):
        result *= x
    return result
 
for i in range(36):
    print(i, factorial(i))
'''