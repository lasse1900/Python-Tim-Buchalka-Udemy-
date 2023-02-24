#
#         012345678901234
parrot = "Norwegian Blue"

print(parrot)

print(parrot[3])

print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print()

print(parrot[-1])
print(parrot[-14])

print()

for i in range(0, len(parrot)):
    print(parrot[i], end=" ")

print('-----------------')
print(parrot[3 - 14])
print(parrot[4 - 14])
print(parrot[9 - 14])
print(parrot[3 - 14])
print(parrot[6 - 14])
print(parrot[8 - 14])

print('-----------')
print(parrot[0:6])
