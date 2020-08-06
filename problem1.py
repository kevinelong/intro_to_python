# Make change
# unlimited number of coins
#

COINS = [25, 10, 5, 1]


def make_change(goal):
    change_to_give = {}

    # while remaining is greater than zero:
    # go through denominations from largest to smallest

    # while remaining less than denomination
    # add quanity until difference less than denomination
    remaining_pennies = goal
    for coin in COINS:  # visit each denom
        while remaining_pennies >= coin:  # determine if current denom issmaller than pennies remain
            remaining_pennies -= coin  # pennies remaining
            if coin not in change_to_give:
                change_to_give[coin] = 0
            change_to_give[coin] += 1
    return change_to_give


print(make_change(93))

# EXPECTED OUTPUT:
# { 25:3, 10:1, 5:1, 1:3 }

print(make_change(76))
# EXPECTED OUTPUT:
# {25: 3, 1: 1}

print(make_change(200))
# EXPECTED OUTPUT:
# {25: 8}