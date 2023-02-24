# Exercise Fizz-Buzz number 17
# https://www.udemy.com/course/python-the-complete-python-developer-course/learn/quiz/4995884#questions/13879328
LOW = 1
HIGH = 100

def fizz_buzz(input: int) -> str:

    """
    Game asks numbers returning `fizz` if input is divisible by 3
        retuns `buzz` if input divisible by 5
        and `fizz buzz` if divisible by 3 and 5
    :input `ìnt`
    :param input_number:
    :return: string according to division by 3 or 5 or both
    """

    if input % 15 == 0:
        return "fizz buzz"
    elif input % 3 == 0:
        return "fizz"
    elif input % 5 == 0:
        return "buzz"
    else:
        return str(input)


for number in range(LOW, HIGH + 1):
    print(fizz_buzz(number))


