import random

index = -1
words = ("python", "jumble", "hideout", "mamacita")

word = random.choice(words)
word_len = len(word)
guess = ""
attempt = 0
enter = ""
temp = "_" * word_len

print("The word chosen by the computer contains", word_len,"letters.")
print("Type any letter to check if this letter is in the chosen word.")
print("You have 5 attempts to check if the letter you typed is in the word chosen by the computer.")

for i in range(0, 5):
    attempt += 1
    guess = input("Attempt no. " + str(attempt) + ": ")
    if guess in word and guess != enter:
        for i in range(0, word_len):
            if guess == word[i]:
                temp = temp[:i] + guess + temp[i + 1:]
        print("yes " + temp)
    if guess not in word:
        print("no")
    if "_" not in temp:
        print("Congratulations!! You guessed the word!")
        break
    elif attempt == 5:
        guess = input("And the word is: ")
        if guess == word:
            print("Congratulations!! You guessed the word!")
        else:
            print("Wrong!! Shame on you!")
