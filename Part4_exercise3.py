import time

# Print our messages based on condition

# some_seconds = 3
# for countdown in reversed(range(some_seconds + 1)):
#     if countdown > 0:
#         print(countdown, end='...')
#         time.sleep(1)
#     else:
#         print('Here is a message: Stay hydrated! :) ')

# -------

# condition = input("Please type 'hello': ")
#
# if condition == "hello":
#     print("You typed: hello!")
# else:
#     #print("You typed something else.")
#     pass



num = int(input("Please give me an even number to print out all its divisors: "))

def printDivisors(n):
    i = 1
    if(n % 2) == 0:
        while i <= n:
            if (n % i==0):
                print(i),
            i = i + 1
    else:
        pass

printDivisors(num)