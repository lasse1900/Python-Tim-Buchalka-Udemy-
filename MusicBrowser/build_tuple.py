def build_tuple(*args):
    return (args)

message_tuple = build_tuple("hello", "planet", "earth","take","me","to","your","leader")
print(type(message_tuple))
print(message_tuple)

number_tuple = build_tuple(1,2,3,4,5,6)
print(type(number_tuple))
print(number_tuple)


def return_string(*args):
    return (args[::-1])

message = return_string("hello", "planet", "earth", "take", "me", "to", "your", "leader")
print(message)

