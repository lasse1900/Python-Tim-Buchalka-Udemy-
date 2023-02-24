'''
books = {"recipes": {"blt": ["bacon", "lettice", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled_eggs": ["eggs", "butter", "milk"],
                    "soup": ["ton of soup"],
                    "paste": ["pasta", "cheese"]},
        "maintenance":{"stuck": ["oil"],
                       "loose": ["gaffer tape"]}}

print(books["recipes"]["soup"])
print(books["recipes"]["scrambled_eggs"])

print(books["maintenance"],["loose"])
'''


import shelve

books = shelve.open("book")
books["recipes"] = {"blt": ["bacon", "lettuce", "tomato", "bread"],
                    "beans_on_toast": ["beans", "bread"],
                    "scrambled eggs": ["eggs", "butter", "milk"],
                    "soup": ["tin of soup"],
                    "pasta": ["pasta", "cheese"]}
books["maintenance"] = {"stuck": ["oil"],
                        "loose": ["gaffer tape"]}

print(books["recipes"])
# print(books["recipes"]["scrambled eggs"])
#
#  print(books["maintenance"]["loose"])
books.close()


