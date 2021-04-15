#  3. Artifact Three
limit = 6
for r in range(1,limit):
    for c in range(limit - r - 1):
        print(".", end="")

    for c in range(r * 2 - 1):
        print("*", end="")
    print("")