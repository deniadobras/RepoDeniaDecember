import random

#Exercise1 - print random words

words = ["cat", "dog", "dinosaur", "random", "words"]

for i in range(len(words)):
    random_index = random.randrange(len(words))
    print(words.pop(random_index))


print("-------------------------------")

#Exercise2 - sum of all float and int in a list

import ast

l = [1, 2, [3, 4, [5, 6, "hello"]], 7, (113, 123.2, [20.4, {"hello" : 5}, 5]), 8, {"10": "bla"}, [9, [10]]]

output = []

def reemovNestings(l):
    for i in l:
        if type(i) == list:
            reemovNestings(i)
        else:
            output.append(i)


print('The original list: ', l)
reemovNestings(l)

print('The list after removing nesting: ', output)

newstr = ','.join([str(elem) for elem in output])
print("this is newstr: ", newstr)

bad_chars = [';', ':', '!', "*", "h", "e", "l", ")", "(", "b", "{", "}", "o", "a", "'", " ", "[", "]", "f", "c", "d", "\\",'"']

test_string = ''.join(i for i in newstr if not i in bad_chars)
print("This is the clean string: ", test_string)

string = test_string.replace(',,', ',')
print("the string:", string)

res = ast.literal_eval(string)
print("final list", res)
print(sum(res))



