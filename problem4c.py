def reverse_list(input_list):
    half = len(input_list) // 2
    for offset in range(0, half):
        temp = input_list[offset]
        input_list[offset] = input_list[offset - 1]
        input_list[offset - 1] = temp

        # input_list[offset], input_list[offset - 1] = input_list[offset - 1], input_list[offset]

    return input_list

def reverse_me(input_text):
    return "".join(reverse_list(list(input_text)))


result = reverse_me("ABC")
print(result)
assert ("CBA" == result)
