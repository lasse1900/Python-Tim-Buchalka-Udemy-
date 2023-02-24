print("Today is a good day to start learn Python")

print('Python is fun')

print("Python's strings are easy to use")

print('We can use "quotes" in strings')

print("hello" + " world")  # string catenation

greeting = "Hello"
# name = input("Please input your name ")
name = "Lasse"

# if we want a space, we can add it too

print(greeting + ' ' + name)

age = 24
print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
# print(name + " is " + age + " years old")

print(name + f" is {age} years old ")
print(type(age_in_words))

print(f"Pi is approximately {22 / 7:12.50f}")
pi = 22 / 7
print(f"Pi is approximately {pi:12.50f}")

print('--------->')

quantity = 10
price = 5.0
total = quantity * price
print("total", total)
tax = total / 5
print("tax: ", tax)

Total = total + tax

print(total)

days = "Mon, Tue, Wed, Thu, Fri, Sat, Sun"
print(days[::5])

data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
print(data[::5])
print(data[1:5])
print(data[0:-1:5])
print(data[:-1:5])