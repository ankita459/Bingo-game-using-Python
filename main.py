import random

# generate a random number between 0 and 99
number = random.randint(0, 99)

# ask the user to guess the number
guess = int(input("Guess a number between 0 and 99: "))

# check if the guess is correct
if guess == number:
    print("Bingo!")
else:
    print("Better Luck Next Time!")
