# REVIEW COLLECTIONS

# LIST

data = [
    "Apple",
    "Orange",
    "Pear",
]

output = {}

for item in data:
    output[item] = item

print(output)

# dict as poor mans class
animals = [
    {
        "name": "Toby",
        "breed": "Lab",
        "age": 15
    },
    {
        "name": "Bianca",
        "breed": "Tortamese",
        "age": 4
    },
]
for a in animals:
    print(a["name"])
    print(a["breed"])
    print(a["age"])
    print("")