filepath = "/Users/denia.dobras/RepoDeniaDecember/text.txt"

with open(filepath,"r+") as file:
    wordcount = {}
    for word in file.read().split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1
print(wordcount)
