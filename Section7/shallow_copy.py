import copy

animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinled"],
    "teddy": ["cuddly", "stuffed"],
}
things = animals.copy()
# animals["teddy"] = "toy"

print(things["teddy"])
print(animals["teddy"])

print()

things["teddy"].append(("toy"))
print(things["teddy"])
print(animals["teddy"])