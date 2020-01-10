# Guess a random number between 1 and 9

import random

target_number, guess_number = random.randint(1, 9), 0

while target_number != guess_number:
    guess_number = int(input("Guess a number between 1 and 9: "))
print("Well guessed!")

