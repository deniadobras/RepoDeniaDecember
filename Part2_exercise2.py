import sys
from select import select
import time

#Exercise 2 - print your name, I misunderstood a bit here and made
# it to wait 3 seconds for the user input, and if there is none, it will end the program.


print("Hi! My name is Denia. Press enter below to end this program:", end='')
timeout = 5
rlist, wlist, xlist = select([sys.stdin],[],[],timeout)
if rlist:
    print("\nThank you!")
else:
    print("\nToo late! Bye!")

# -----------------

# Version2 - waits 3 seconds after the user input to end the program

# input("Hi! My name is Denia! Please press enter to finish the program: ")
# time.sleep(3)
# print("\nProgram ended after 3 seconds")