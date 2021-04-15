data = [
    {
        "name": "Toby",
        "kind": "Dog",
        "breed": "LabDaneMix"
    },
    {
        "name": "Bianca",
        "kind": "Cat",
        "breed": "Tortamese"
    }
]

for item in data:
    print(item["name"])

# SIMPLE: also print kind and breed
for item in data:
    print(item["name"])
    print(item["kind"])
    print(item["breed"])

# ADVANCED: when complete print the number of items printed

print(f"TOTAL PRINTED: { len(data)}")


# EXTRA: convert to a function

def show(data):
    counter = 0
    for item in data:
        # print(item["name"])
        # print(item["kind"])
        # print(item["breed"])
        # print(item["name"] + " " + item["kind"] + " " + item["breed"])

        print(f'{item["name"]} {item["kind"]} {item["breed"]} ', end="\n\n")

        print("")  # extra blank line inside the loop
        counter = counter + 1
        # counter += 1
    print("---")
    print(f"TOTAL PRINTED: { counter }")


show(data)


class Dog:
    # Constructor
    def __init__(self, name):
        self.name = name
