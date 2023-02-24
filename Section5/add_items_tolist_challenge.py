data = [
    "Andromeda - Shrub",
    "Bellflower - Flower",
    "China Pink - Flower",
    "Daffodil - Flower",
    "Evening Primrose - Flower",
    "French Marigold - Flower",
    "Hydrangea - Shrub",
    "Iris - Flower",
    "Japanese Camellia - Shrub",
    "Lavender - Shrub",
    "Lilac - Shrub",
    "Magnolia - Shrub",
    "Peony - Shrub",
    "Queen Anne's Lace - Flower",
    "Red Hot Poker - Flower",
    "Snapdragon - Flower",
    "Sunflower - Flower",
    "Tiger Lily - Flower",
    "Witch Hazel - Shrub",
]

flowers = []
shrubs = []

'''
for item in data:
    if "Flower" in item:
        flowers.append(item[:-9])
    elif "Shrub" in item:
        shrubs.append(item[:-9])
'''


for plant in data:
    if "Flower" in plant:
        flowers.append(plant)
    elif "Shrub" in plant:
        shrubs.append(plant)



print(flowers)
print(shrubs)