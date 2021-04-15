# Pick a number
# I am thinking of a number between 1 and 100
# tell me your guess, and I will saw you are too high or too low.
import random
secret = random.randint(1,100)
guess = -1
print(secret)

while guess != secret:
    text = input("guess:")
    guess = int(text)
    #TODO tell user if number is too high or too low using "if" an "print"

    if guess < secret:
        print("too low")

    elif guess > secret:
        print("too high")

    elif guess == secret:
        print("Yayyy!!!")

print(f"Correct! it was {secret}")
# print("Correct! it was " + secret)

