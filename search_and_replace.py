#REPLACE FRAGMENTS IN A TEXT STRING
text = "Now is the time for all good people to come to the aid of their party."
fixed = text.replace("party", "planet")
print(fixed)

print(fixed.replace(" ", "-"))

# REPLACE ITEMS IN A LIST
data = [
    "apple",
    "orange",
    "apple",
    "pear",
    "apple",
]

output = []
for item in data:
    if item == "apple":
        output.append("banana")
    else:
        output.append(item)

print(output)