import sys

def getFloat(prompt):
    while True:
        try:
            return float(input(prompt))
        except EOFError:
            sys.exit(1)
        except: # Should really be except ValueError
            print("Not a valid number!")
        finally:
            print("The finally clause always executes")

first = getFloat("Give a number to be divided: ")
second = getFloat("Give second number, divider: ")

try:
    result = first / second
    print(f"{first} divided by {second} is: {result}")
except ZeroDivisionError:
    print("Not possible to divide by zero")
    sys.exit(2)
else:
    print("Division performed succesfully")


