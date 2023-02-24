
def is_palindrome(string: str) -> bool:
    """
    Checks if string is a palindrome
    :param : a string to be checked
    :return: returns True if string is a palindrome otherwise returns False
    """
    return string[::-1].casefold() == string.casefold()


string = input("Please enter a string to check if palindrome: ")
if is_palindrome(string):
    print("'{}' is a palindrome".format(string))
else:
    print("'{}' is a not palindrome".format(string))


# p = is_palindrome()
