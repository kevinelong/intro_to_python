
name = input("What is your name?")

print(f"\nHello {name}!!!")

total = 0

text = "default"

while text != "":
    text = input("Enter number or blank line to quit:")

    if text != "":
        number = int(text)
        total += number
        print(total)

print("Thanks!")
