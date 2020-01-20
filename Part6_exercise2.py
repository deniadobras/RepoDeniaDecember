#Exercise2 - list of first and last - how do I make a new list with these 2 numbers?

a = [5, 10, 15, 20, 25]

def list_ends(list):
    return [list[0], list[len(list)-1]]

print(list_ends(a))