# https://docs.python.org/3/library/stdtypes.html#set

small_int = set(range(21))
print(small_int)

# small_int.clear()
# print(small_int)

small_int.discard(10)
small_int.remove(11)
print(small_int)

small_int.discard(99)
print(small_int)

small_int.remove(99)
print(small_int)