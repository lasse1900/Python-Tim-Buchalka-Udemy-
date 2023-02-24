#          01234567890123456789012345
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
# backwards = letters[25::-1]
print(backwards)

# 1
# qpo = letters[16] + letters[15] + letters[14]
# print(qpo)
print(letters[16:13:-1])

# 2
print('--------2----------')
ebcda = letters[4::-1]
print(ebcda)

# 3
print('------3-------')
last_8_chars = letters[:25-8:-1]
print(last_8_chars)
print(letters[:-9:-1])

print('----------')
print(letters[-4:])
print(letters[-1:])
print(letters[:1])
# print(letters[0]) Producers Error
