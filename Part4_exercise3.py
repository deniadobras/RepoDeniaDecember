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


num = 0


def divisors(number):
    n = 1
    while (n < number):
        if (number % n == 0):
            print(n)
        else:
            pass
        n += 1
    print(number)


while True:
    try:
        if type(num) == int:
            num = int(input("Please give me an even number to print out all its divisors: "))
            divisors(num)
            break
    except ValueError:
        print("Please only use ints.")
