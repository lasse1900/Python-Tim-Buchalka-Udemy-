data = [1,4,5,12,21,76,103,210,223, 405,505,506]

for index, user in enumerate(data):
    if index == 3:
        print("Extra verbose output for:", index, data)
        print(user)

'''
grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print('\n')

for count, item in enumerate(grocery):
  print(count, item)

print('\n')
# changing default start value
for count, item in enumerate(grocery, 100):
  print(count, item)
'''

'''
grocery = ['bread', 'milk', 'butter']
enumerateGrocery = enumerate(grocery)

print(type(enumerateGrocery))

# converting to list
print(list(enumerateGrocery))

# changing the default counter
enumerateGrocery = enumerate(grocery, 10)
print(list(enumerateGrocery))
'''


users = ["Test User", "Real User 1", "Real User 2"]
for index, user in enumerate(users):
    if index == 1:
        print("Extra verbose output for:", user)
        print(user)

