"""MASHQLAR"""

# 052

import random

num = random.randint(1, 100)
print(num)

# 053

fruits = random.choice(["Apple", "Banana", "Chivi", "Gilos", "Mandarin"])
print(fruits)

# 054

coin = random.choice(["h", "t"])
guess = input("Enter (h)eads or (t)ails: ")
if guess == coin:
    print("You WIN!")
else:
    print("Bad luck")
if coin == "h":
    print("it was heads")
else:
    print("It was tails")

# 055

num = random.randint(1, 5)
guess = int(input("Son tanlang: "))
if guess == num:
    print("Well done")
elif guess > num:
    print("Too high")
    guess = int(input("Guess again: "))
    if guess == num:
        print("Correct")
    else:
        print("You lose")
elif guess < num:
    print("Too low")
    guess = int(input("Guess again: "))
    if guess == num:
        print("Correct")
    else:
        print("You lose")

# 056 

num = random.randint(1, 10)
Correct = False
while Correct == False:
    guess3 = int(input("Son kirit: "))
    if guess3 == num:
        Correct == True
