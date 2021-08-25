data = [
    1, 1, 1, 5, 5, 5, 5, 10, 25, 25, 100
]
# output = {
#     1: 0,
#     5: 0,
#     10: 0,
#     25: 0,
# }
output = {}
for coin in data:
    if coin not in output:
        output[coin] = 0
    output[coin] += 1

print(output)
#####

quantities = {
    1: 3,
    5: 4,
    10: 1,
    25: 2
}

total = 0
for k in quantities:
    v = quantities[k]
    total += k * v
    print(k, v)
print(total)