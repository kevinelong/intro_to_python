def show_ascii(name):
    for letter in name:
        ascii_code = ord(letter)
        print(ascii_code, letter)


show_ascii("ABC")
