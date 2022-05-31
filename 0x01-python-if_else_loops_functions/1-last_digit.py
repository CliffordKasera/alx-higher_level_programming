#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    last = number % 10
else:
    last = ((number * -1) % 10) * -1
word = f"Last digit of {number:d} is {last:d}"
if last > 5:
    print(word, "and is greater than 5")
elif last == 0:
    print(word, "and is 0")
else:
    print(word, "and is less than 6 and not 0")
