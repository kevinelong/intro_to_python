first = ["a", 123, [1, 2, 3]]
second = ["a", 123, [1, 2, 3]]

existing = [first]
if second not in existing:
    existing.append(second)
# print(first == second)

print(existing)
