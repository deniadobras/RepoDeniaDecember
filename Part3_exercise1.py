import numpy as np
from decimal import Decimal
import numpy

# program that counts for the user. Let the user enter the starting number, the ending number, and the amount by which to count.

# minimum = int(input("Enter the start of range: "))
# maximum = int(input("Enter the end of range: "))
# amount = int(input("Enter the range: "))
#
#
# for i in range(minimum, maximum + 1, amount):
#     print(i, end=' ')
import sys

try:
    minimum = int(input("Enter the start of range: "))
    maximum = int(input("Enter the end of range: "))
    amount = int(input("Enter the range: "))

    for i in numpy.arange(minimum, maximum + 1, amount):
        print(i, end=' ')

except ValueError:
    print("Please only use numbers to count.")

