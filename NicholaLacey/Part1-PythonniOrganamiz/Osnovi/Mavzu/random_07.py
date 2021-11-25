""" Random sonlar """

"""
random sonni ishlatish uchun:
'random kutubkonasini import qolish kerak'
---import random
"""

""" MAVZUGA OYID MISOLLAR """

from math import pi
import random 
# num = random.random()
# num = num * 100
# print(num)

# num = random.randint(0, 9) # 0, 9 oraligidagi random sonlarni Oladi!

num1 = random.randint(0, 1000)
num2 = random.randint(0, 1000)
newrand = num1 / num2
print(newrand)

#num = random.randrange(0, 100, 5) # 0, 100gacha bolgan oraligidagi random sonlarni Oladi va 5 pogona hatordan oladi
# yani 0, 5, 10, 15, 20 va h.k

colour = random.choice(["red", "black", "green"]) # listdagi hohlagan qiyamtini oladi 


