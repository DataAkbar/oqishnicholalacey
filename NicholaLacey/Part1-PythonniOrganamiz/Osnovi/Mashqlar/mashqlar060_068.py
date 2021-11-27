# 060

from operator import imod
import turtle
from typing import IO

turtle.bgcolor("pink")
turtle.shape("turtle")

# for i in range(0, 4): # Tort burchak
    
#     turtle.forward(100)
#     turtle.right(90)

# turtle.exitonclick()

# 061

# for i in range(0, 3): # Uch burchak 

#     turtle.forward(100)
#     turtle.left(120)

# turtle.exitonclick()

# 062

# for i in range(0, 360): # aylana
#     turtle.forward(1)
#     turtle.right(1)

# turtle.exitonclick()

# 063

# import turtle

# birinchi qarobka
# turtle.color('black', "red")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(70)
#     turtle.right(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)

# turtle.pendown() # ikkinchi qarobka
# turtle.color("black", "yellow")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(70)
#     turtle.right(90)
# turtle.penup()
# turtle.end_fill()
# turtle.forward(100)

# turtle.pendown() # uchunchi karonka
# turtle.color("black", "green")
# turtle.begin_fill()
# for i in range(0, 4):
#     turtle.forward(70)
#     turtle.right(90)
# turtle.end_fill()
# turtle.exitonclick()

# 064

# import turtle
# turtle.begin_fill()

# for i in range(0, 5):
#     turtle.forward(200)
#     turtle.right(144)
# for i in range(0, 5):
#     turtle.begin_fill()
#     turtle.forward(200)
#     turtle.left(144)
# turtle.end_fill()
# turtle.exitonclick()


# import turtle as t

# t.left(90)
# t.forward(100)
# t.right(90)
# t.penup()
# turtle.forward(50)
# t.pendown()
# t.forward(75)
# t.right(90)
# t.forward(50)
# t.right(90)
# t.forward(75)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(75)
# t.penup()
# t.forward(50)
# t.pendown()
# t.forward(75)
# t.left(90)
# t.forward(50)
# t.left(90)
# t.forward(45)
# t.left(180)
# t.forward(45)
# turtle.left(90)
# turtle.forward(50)
# t.left(90)
# turtle.forward(75)

# turtle.hideturtle()

# t.exitonclick()

#066

# import turtle
# import random

# turtle.pensize(3)

# for i in range(0, 8):
#     turtle.color(random.choice(["red", "blue", "yellow", "green", "black", "orange"]))
#     turtle.forward(50)
#     turtle.right(45)

# turtle.exitonclick()

# 067

import turtle
import random

for i in range(0, 10):
    for i in range(0, 8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)

turtle.hideturtle()

turtle.exitonclick()

# 068

# import turtle
# import random

# lines = random.randint(5, 20)

# for i in range(0, lines):
#     lenght = random.randint(25, 100)
#     rotate = random.randint(1, 365)
#     turtle.forward(lenght)
#     turtle.right(rotate)

# turtle.exitonclick()