""" MASHQLAR """

# 012

# num1 = int(input("Iltimos istagan soningizni kiriting: "))
# num2 = int(input("Iltimos yan bir marta, istagan soningizni kiriting: "))

# if num1 > num2:
#     print (num2)
#     print (num1)
# else:
#     print (num1)
#     print (num2)

# 013

# num = int(input("Iltimos 20dan kam bolgan sonni kiriting: "))

# if num >= 20 :
#     print("Too higt")
# else:
#     print("Thank you, BABY")

# 014 

# num = int(input("Iltimos 10dan 20gacha bolgan sonni kiriting: "))

# if num >= 10 and num <= 20:
#     print ("Thanks baby")
# else:
#     print ("Inkorreckt answer")

# 015

# colour = input("Sizning sevimli rangingiz?: ")

# if colour == "RED" or colour == "red" or colour =="Red":
#     print ("I like red too")
# else:
#     print ("I dont like, colour, I prefer red")


# 016 

message = input("Yomg'r yog'ayaptimi?: ")
message = str.lower(message)

if message == "yes":
    sorov = input("Shamol bormi kochada?: ")
    sorov = str.lower(sorov)
    if sorov == "yes":
        print("It is too windy for an umbrella")

    else:
        print("Take an umbrella")

else:
    print("Enjoy your day")