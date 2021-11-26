"""MASHQLAR"""

# 052

# from _typeshed import ReadableBuffer
# from operator import truediv
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
        Correct = True

# 057

num = random.randint(1, 10)
Correct = False
while Correct == False:
    guess3 = int(input("Son kirit: "))
    if guess3 == num:
        Correct = True
    elif guess3 > num:
        print("Too high")
    else:
        print("Too low")

# 058
print("058")

import random 
score = 0 
for i in range(1, 6):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    currect = num1 + num2 
    print(num1, "+", num2, "= ")
    answer = int(input("You answer: "))
    print()
    if answer == currect:
        score = score + 1
print("You scored ", score, " out of 5")

# 059

colour = random.choice(["red", "blue", "green", "white", "pink"])
print("Select from red, blue, green, white, or pink")
tryagain = True 
while tryagain == True:
    theirchois = input("Enter a colour: ")
    theirchois = theirchois.lower()
    if colour == theirchois:
        print("Well done")
        tryagain = False
    else:
        if colour == "red":
            print("I bet you seeing RED right now!")
        elif colour == "blue":
            print("Don't feel BLUE>")
        elif colour == "green":
            print("I bet you are green whis envy right now!")
        elif colour == "white":
            print("Are you WHITE as a sheet, as you didn't guess curretly?")
        elif colour == "pink":
            print("Some one you are not feeling in thr PINK, \
                as you got it wrong!")
                