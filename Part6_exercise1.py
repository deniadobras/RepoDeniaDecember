
# calculate sum of n numbers

# def my_sum(inputNumbers):
#     for x in inputNumbers:
#         return sum(inputNumbers)
#
# inputNumbers = [1, 2, 3]
#
#
# print(my_sum(inputNumbers))
#
# for n in range(1, 10):
#     print(n)
#
# print(sum(inputNumbers))

#n = int(input("Enter a number to calculate sum: "))
n = 0

def calculate_sum(n):
    n = int(input("Enter a number to calculate sum: "))
    sum = n * (n+1) / 2
    print("Sum of the first", n, "natural numbers is: ", sum )

try:
    if type(n) == int:
        calculate_sum(n)
except ValueError:
    print("Please input only ints.")
