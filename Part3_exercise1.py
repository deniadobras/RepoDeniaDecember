
minimum = int(input("Enter the start of range: "))
maximum = int(input("Enter the end of range: "))
amount = int(input("Enter the range: "))


for i in range(minimum, maximum + 1, amount):
    print(i, end=' ')
