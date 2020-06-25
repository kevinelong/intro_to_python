# Selects an integer between 1 and 10
from random import randint

secret = randint(1, 10)

print("I am thinking of a secret number between 1 and 10.")
print("Guess and I will tell you if you are high, low, or just right.")

guess: int = 0

while guess != secret:

    print("What is your guess?")
    # Read a line of user input text from the Console into a String.
    i = input()

    if i:
        guess = int(i)

    if guess > secret:
        print(f"Your guess {guess} is greater than secret.")
    elif guess < secret:
        print(f"Your guess {guess} is less than secret.")

print(f"Perfect. You are right! {secret} is correct.")
