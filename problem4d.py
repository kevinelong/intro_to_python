def reverse_list(input_list):
    input_list.reverse()
    return input_list


def reverse_me(input_text):
    it = list(input_text)
    rl = reverse_list(it)
    return "".join(rl)

data = "ABC"
result = reverse_me(data)
print(result)
assert ("CBA" == result)
print(data)