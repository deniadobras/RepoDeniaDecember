

def my_sum(inputNumbers):
    for x in inputNumbers:
        return sum(inputNumbers)

inputNumbers = [1, 2, 3]


print(my_sum(inputNumbers))

for n in range(1, 10):
    print(n)



print(sum(inputNumbers))

n = input("Enter a number to calculate sum: ")

n = int(n)
sum = n * (n+1) / 2

print("Sum of the first ", n, "natural numbers using formula is: ", sum )
