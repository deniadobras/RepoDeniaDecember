import random

#Exercise1 - print random words

words = ["cat", "dog", "dinosaur", "random", "words", "words"]

for i in range(len(words)):
    random_index = random.randrange(len(words))
    print(words.pop(random_index))


