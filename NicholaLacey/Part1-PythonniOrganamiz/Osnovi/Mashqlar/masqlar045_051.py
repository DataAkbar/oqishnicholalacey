# 045

total = 0
while total <= 50:
    num = int(input("Son kiriting: "))
    total = total + num
    print("The total is ", total)

# 046 

num = 0
while num < 5:
    num = int(input("Son kiriting -"))
print("The last number you entered was a", num)

# 047

num1 = int(input("1) Sonni kiriting: "))
total = num1
again = "y"
while again == 'y':
    num2 = int(input("Yana bir marta son kiritining "))
    total = total + num2
    again = input("Do you want to add another number? (y/n)")
print("The total is ", total)

# 048

again = "y"
count = 0
while again == "y":
    name = str(input("Kechaga chaqirmoqchi bolgan insonni ismini yozing: "))
    print(name, " has be invited")
    count = count + 1
    again = input("Do you want to invite somebody else? (y/n)")
print("You have ", count, " people coming to your party")

# 049

compnut = 50
guess = int(input("Son kiriting: "))
count = 0
while guess != compnut:
    if guess < compnut:
        print("Too low")
    else:
        print("Too high")
    count = count + 1
    guess = int(input("Have another gueess: "))
print("Well done, you took ", count, " attempts")


# 050

nums = int(input("10dan 20gacha bolgan sonni kiriting: "))
while nums < 10 and nums > 20:
    if nums < 10:
        print("Too low")
    else:
        print("Too high")
    num = int(input("Yana urunub koring: "))
print("Thank you!")

# 051

num = 10 
while num > 0:
    print("There are ", num, " green bottles handing on the wall.")
    print( num, " green bottles hanging on the wall.")
    print("And if 1 green bottle should accidentally fall,")
    num = num + 1
    answer = int(input("how many green botless will be handing on the wall? "))
    if answer == num:
        print("the will be ", num, ' green botlessm handing on the wall.' )
    else:
        while answer != num:
            answer = int(input("No, try again: "))
print("There are no more green bottles handing on the wall.")

