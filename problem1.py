# We have a change drawer with unlimited change,
# what is the most efficient way to give
# a specific amount of change

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


print(make_change(93))

# data = {
#     1: 3,
#     5: 1,
#     10: 1,
#     25: 3,
# }
