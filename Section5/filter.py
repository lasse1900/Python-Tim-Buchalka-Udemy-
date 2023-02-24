menu = ["bacon","spam","lettice", "tomato","spam"]

filtered = []

for meal in menu:
    if meal != "spam":
        filtered.append(meal)

print(filtered)