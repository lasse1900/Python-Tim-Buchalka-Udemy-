def python_food():
    width = 80
    text = "Spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text_0(text):
    text = str(text)
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text)

def centre_text_0(*args, sep=' ', end='\n', file=None, flush=False):
    text = " "
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


def centre_text(*args, sep=' '):
    text = " "
    for arg in args:
        text += str(arg) + sep
    left_margin = (80 - len(text)) // 2
    # print(" " * left_margin, text, end=end, file=file, flush=flush)
    return " " * left_margin + text

print('-' * 50 + " -> into File")
with open("centred", mode='w') as centred_file:
    centre_text_0("spam and eggs", file=centred_file)
    centre_text_0("spam, spam and eggs", file=centred_file)
    centre_text_0(12, file=centred_file)
    centre_text_0("spam, spam, spam and eggs", file=centred_file)
    centre_text_0("first", "second", 3, 4, "spam", sep=':', file=centred_file)

print('-' * 50 + " -> print to console")
# Call the function
# print(centre_text("spam and eggs"))
# print(centre_text("spam, spam and eggs"))
# print(centre_text(12))
# print(centre_text("spam, spam, spam and eggs"))
# print(centre_text("first", "second", 3, 4, "spam", sep=':'))

with open("menu", "w") as menu:
    s1 = centre_text("spam and eggs")
    print(s1, file=menu)
    s2 = centre_text("spam, spam and eggs")
    print(s2, file=menu)
    print(centre_text(12), file=menu)
    s4 = centre_text_0("spam, spam, spam and eggs", file=menu)
    print(s4)