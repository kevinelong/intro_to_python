data = [
    {
        "name": "kevin",
        "age": 29,
    },
    {
        "name": "nina",
        "age": 19,
    }
]

for p in data:
    if p["age"] >= 21:
        print(f"{p['name']} can")
    else:
        print(f"{p['name']} can't")
