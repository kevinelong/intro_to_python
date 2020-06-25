# Write a function named reverse_me that
# takes a string as a parameter,
# and returns the reversed string.
#
# Do this without using pythons [::-1] slice shortcut,
# or the built in reversed() method
#
# You will need to count down from the length of the string,
# and build up the output one piece at a time.
#
# The input ABC should return BCA as output


def reverse_me(input_text):

    output = ""

    text_length = len(input_text)

    offset = 0

    while offset < text_length:
        index = text_length - offset - 1
        letter = input_text[index]
        output = output + letter
        offset += 1

    return output


# TEST

result = reverse_me("ABC")
assert ("CBA" == result)


#DEMO
# print("ENTER TEXT TO BE REVERSED:")
# data = input()
# result = reverse_me(data)
# print(result)
