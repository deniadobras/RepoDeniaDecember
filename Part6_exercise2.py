#Exercise2 - list of first and last - how do I make a new list with these 2 numbers?

a = [5, 10, 15, 20, 25]
c = []

def my_function(b):
    # print([a[0], a[-1]])
    c = list(a[0], a[-1])

print(my_function(c))
