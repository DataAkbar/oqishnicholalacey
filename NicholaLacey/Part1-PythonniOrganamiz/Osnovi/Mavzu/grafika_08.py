""" TOSHBAQALI GRAFIKA """

"""
Объяснение
В Python можно рисовать с использованием черепахи (turtle).
Используя различные команды и циклы, можно строить сложные изображения.
Вот как это работает.

Черепаха перемещается по определяемому вами пути, оставляя за собой след. 
В то время когда вы управляете черепахой, на изображении за ней остается 
видимый след. Чтобы нарисовать пятиугольник, изображенный ниже, следует 
ввести следующий код.
"""
import turtle

turtle.shape("turtle")

# for i in range(0, 5):
#     turtle.forward(100)
#     turtle.right(72)

# turtle.exitonclick()

for i in range(0, 10):
    
    turtle.right(36)
    
    src = turtle.Screen()
    
    src.bgcolor("blue")

    turtle.color("yellow", "red")

    for i in range(0, 5):
        turtle.forward(100)
        turtle.right(72)

turtle.exitonclick()

