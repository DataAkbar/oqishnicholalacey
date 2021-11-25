"""Chuntirish"""

# if qollanmasi sizn shartlar bilan ishlaysiz 

# Pythonda if qollanmasi ko'rinishi:
# while True: # While siklini ozim qoshdim!
num1 = float(input(':'))

if num1 > 10:
    print ("This is over 10")
elif num1 == 10:
    print ("this is equal to 10")
else:
    print ("This is under 10")
        # break # siklni tamom etadi

"""Operatorlar"""

"""

Takoslash Operatori:

== - Teng

!= - Teng emas

< - Katta

> - Kichik

>= - Katta yoki teng

<= - Kichik yoki teng

LOGIK OPERATORLAR:

and - Ikkita shart bir vaqtda bajarilishi kerak

or - Hech bolmaganda IKKITASINDAN BIRI shart bajarilishi kerak

"""

"""MISOLLAR"""

num1 = int(input("-:"))
if num1 >= 10:
    if num1 <= 20:
        print ("This is between 10 and 20") # 20 bilan 10ni orasinda bolsa shu chiqadi
    else:
        print ("This is over 20") # 20dan katta bolsha chiqadi
else:
    print ("This is under 10") # 10dan kichik bol'sa

num1 = int(input("Enter a number beetwewn 10 and 20: "))

if num1 >= 10 and num1 <= 20:
    print("Thank you, baby")

else:
    print ("Out of range")


num = int(input("Enter an EVEN number beetwewn 1 and 5: "))

if num == 2 or num == 4:
    print("Thanks")

else:
    print("Incorrect")