#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    lastnum = number % 10
elif number < 0:
    lastnum = number % -10
else:
    lastnum = 0
if lastnum == 0:
    print(f"Last digit of {number} is {lastnum} and is 0")
elif lastnum > 5:
    print(f"Last digit of {number} is {lastnum} and is greater than 5")
else:
    print(f"Last digit of {number} is {lastnum} and is less than 6 and not 0")
