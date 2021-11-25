"""Primeri koda"""

num1 = 93 # Ozgaruvchan
num2 = 33 # Ozgaruvchan
ansver = num1 + num2  # num1 va num2 ansverga ko'shib yuklaydi

answer = num1 - num2 # num1 va num2 ansverga olib yuklaydi

ansver = num1 * num2 # num1 va num2 ansverga kopaytirib yuklaydi

ansver = num1 / num2 # num1 va num2 ansverga bo'lib yuklaydi

answer = num1 // num2 # num1 va num2 ansverga qoldigini yuklaydi


print('This is a message') # chiqarish

print("First line\nSecond line") # \n - Obzast qilib chiqaradi

print("The answer is ", answer) # answerdagi qiymatni sabsheniya bn chiqaradi

# textValue = input("Enter a text value: ")
# numValue = int(input("Enter a number: "))

# print(textValue, numValue)

"""Misollar"""

# 001 

name = input("O'z ismingizni kiriting: ")
print("Salom", name)

# 002

name = input("O'z ismingizni kiriting: ")
lastname = input("O'z familiyangizni kiriting: ")
print("Salom!,", name, lastname)

# 003

print("What do you call a bear with no teeth\nA gummy bear!")

# 004 

rec0 = input("So'n kiriting: ")
rec1 = input("Yana bir so'n kiriting: ")

print("The total is", rec0 + rec1)

# 005 

rec0 = int(input("So'n kiriting: "))
rec1 = int(input("Yana bir so'n kiriting: "))
rec2 = int(input("Yana bir so'n kiriting: "))

print("The answer is", (rec0 + rec1)*rec2)

# 006

message0 = int(input("Sizda necha Pitsiya qoldig'i bor edi?: "))
message1 = int(input("Siz nechta Pitsiya qoldig'ini yedinigiz?: "))
runi = message0 - message1
print(f"Sizda {runi}ta Pitsiya qoldig'i qoldi")

# 007 

name = input("Sizning isminig nima? ")
age = int(input("Siz necha youshdasiz? "))
newAge = age + 1
print(name,"," 'Sizning keyingi yoshingiz', newAge)

# 008

bill = int(input("What is the total cost of the bill? "))

people = int(input("how many people are there? "))

each = bill / people

print("Each person should pay $", each)

# 009

day = int(input("Enter the number of days: "))
hours = day *24
minutes = hours * 60
seconds = minutes * 60
print("In", day, " Days there are... ")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")

# 010

kilo = int(input("Enter the number of kilos: "))
pound = kilo * 2.204
print("That is ", pound, " pounds")

# 011

large  = int(input("Enter a number 100: "))
smaller = int(input("Enter a number 10: "))
answeri = large // smaller 
print(smaller, " goes into ", large, answer, " times")