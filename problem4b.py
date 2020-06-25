
def reverse_me(input_text):

    output = []

    text_length = len(input_text)

    for offset in range(0, text_length):
        index = text_length - offset - 1
        letter = input_text[index]
        output.append(letter)

    return "".join(output)


result = reverse_me("ABC")
print(result)
assert ("CBA" == result)
