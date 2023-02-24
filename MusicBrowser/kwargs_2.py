# def print_backwards(*args, **kwargs):
#     print(kwargs)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)
#
# with open("backwards.txt","w") as backwards:
#     print_backwards("hello","how","do","you","do", file=backwards, end='\n')


# My solution to Challenge in Lesson 358

# def print_backwards(*args, **kwargs):
#     # print(kwargs)
#     for word in args[::-1]:
#         if 'end' in kwargs:
#             print(word[::-1], **kwargs)
#         else:
#             print(word[::-1], end=' ', **kwargs)
#
# with open("backwards.txt","w") as backwards:
#     print_backwards("hello","how","do","you","do", end='\n')

# Tim's solutions a and b

# def print_backwards(*args, end=' ', **kwargs):
#     print(kwargs)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)
#
# with open("backwards.txt","w") as backwards:
#     print_backwards("hello","how","do","you","do", end='\n')

# def print_backwards(*args, end=' ', **kwargs):
#     print(kwargs)
#     kwargs.pop('end', None)
#     for word in args[::-1]:
#         print(word[::-1], end=' ', **kwargs)
#
# with open("backwards.txt","w") as backwards:
#     print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
#     print("Another string")
#
# print()
# print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n', sep='|')
# print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n', sep='|')

# new version

def print_backwards(*args, **kwargs):
    enc_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for word in args[:0:-1]: # change the range
        print(word[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=enc_character, **kwargs) # and print the first word separately
    # print(end=enc_character) # which means we don't need this line


with open("backwards.txt","w") as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("Another string")

print()
print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 10)

print("=" * 50)
def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::1]), **kwargs)

backwards_print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='|')












