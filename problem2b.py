# REQUIREMENT: total all numbers found in this string
data = "abc=123&def=456&hij=789"

# how can we use split to access and then add the values together
# list
# split - str.split(sep) return a list (will be called twice)
# sum
# for

# TODO add code

# print(123+456+789)
# 1368

# print(sum([123,456,789]))

pairs = data.split(",")
numbers = []
for p in pairs:
    key_and_value = p.split("=")
    string_value = key_and_value[1]
    int_value = int(string_value)
    numbers.append(int_value)
total = sum(numbers)
print(total)
