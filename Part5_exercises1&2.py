#Exercise1 - print random words

words = ["cat", "dog", "dinosaur", "random", "words"]

for x in words:
    print(x)

#Exercise2 - sum of all float an dint in a list (version1) - there are 3 versions here but I am not happy with either of them, so I will have to re-think this one to find an actual solution

alist = ['a', 1, 'f', 3.2, 4, 'abc', ('a', 2, 'c'), [5, 6]]

print(sum([i for i in alist if not (not isinstance(i, int) and not isinstance(i, float))]))

print(alist)

#Exercise2 - sum of all float an dint in a list (version2)


def calsum(l):
    return sum([int(i) for i in l if type(i) == int or i.isdigit()])


list1 = [12, 'geek', 2, '41', 'for', 10, '8', 6, 4, 'geeks', 7, '10']
list2 = [100, 'geek', 200, '400', 'for', 101, '2018', 64, 74, 'geeks', 27, '7810']

print(calsum(list1))
print(calsum(list2))

#Exercise2 - sum of all float an dint in a list (version3)

L = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]


# Using naive method
res = list()
for j in range(0, len(L[0])):
    tmp = 0
    for i in range(0, len(L)):
        tmp = tmp + L[i][j]
    res.append(tmp)

# printing result
print("Final list - ", str(res))






