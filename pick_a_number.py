
# Selects an integer between 1 and 10
from random import randint

playing = True

while playing:
    secret = randint(1, 10)

    print("I am thinking of a secret number between 1 and 10.")
    print("Guess and I will tell you if you are high, low, or just right.")

    guess: int = 0

    while guess != secret:

        # Read a line of user input text from the Console into a String.
        i = input("What is your guess?")

        if i:
            guess = int(i)

        if guess > secret:
            print(f"Your guess {guess} is greater than secret.")
        elif guess < secret:
            print(f"Your guess {guess} is less than secret.")

    print(f"Perfect. You are right! {secret} is correct.")

    entry_incomplete = True
    while entry_incomplete:
        again = input("Press enter 'A' to play again. or enter 'Q' to quit")
        again = again.upper()

        if len(again) > 1:
            print("Single letter only")
        elif len(again) == 0:
            print("Please enter a letter")
        elif again not in ['A', 'Q']:
            print("please enter Q or A")
        else:
            if again == "A":
                playing = True
            elif again == "Q":
                playing = False
            entry_incomplete = False
