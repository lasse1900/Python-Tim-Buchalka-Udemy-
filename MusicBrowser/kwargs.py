def print_backwards(*args, file=None):
    for word in args[::-1]:
        print(word[::-1], end=' ', file=file)

with open("backwards.txt","w") as backwards:
    print_backwards("hello","how","do","you","do", file=backwards)