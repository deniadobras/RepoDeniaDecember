# Guess a random number between 1 and 9

import random

target_number, guess_number = random.randint(1, 9), 0

# while target_number != guess_number:
#     guess_number = int(input("Guess a number between 1 and 9: "))
# print("Well guessed!")

while True:
    try:
        if target_number != guess_number:
            guess_number = int(input("Guess a number between 1 and 9: "))
            if guess_number < 1 or guess_number > 9:
                print("I said a number between 1 and 9, dude!")
                guess_number = int(input("Guess a number between 1 and 9: "))
        else:
            print("Well guessed")
            break
    except ValueError:
        print("Please guess only ints between 1 and 9.")
