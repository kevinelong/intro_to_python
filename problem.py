# data = {
#     1: 13,
#     5: 3,
#     10: 1,
#     25: 1,
# }

DENOMINATIONS = [25, 10, 5, 1]


def make_change(pennies):
    output = {}
    # TODO put code here
    for d in DENOMINATIONS:
        while pennies >= d:
            pennies -= d
            if d not in output:
                output[d] = 0
            output[d] += 1
    return output

# q = [3,1,1,3]
# z = zip(DENOMINATIONS,q)
# print(dict(z))

print(make_change(93))

# data = {
#     1: 3,
#     5: 1,
#     10: 1,
#     25: 3,
# }
