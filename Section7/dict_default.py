from contents import pantry

chicken_quantity = pantry.setdefault("chicken", 0) # vrt get()
print(f"chicken: {chicken_quantity}")

beans_quantity = pantry.setdefault("beans, 0")
print(f"beans: {beans_quantity}")


ketchup_quantity = pantry.get("ketchup", 0)  # is not added
print(f"ketchup: {ketchup_quantity}")

z_quantity = pantry.setdefault("zucchini", "eight") # is added to dict
print(f"zucchini: {z_quantity}")

print()
print("`pantry` now contains...")

for key, value in sorted(pantry.items()):
    print(key, value)
