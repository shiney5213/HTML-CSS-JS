import turtle
import math

width = 100
height = 100
turtle.color("blue")
turtle.pensize(5)
turtle.forward(width)

turtle.left(90)
turtle.forward(height)

turtle.left(90)
turtle.forward(width)

turtle.left(90)
turtle.forward(height)

turtle.left(135)
root = math.sqrt(width **2 + height **2)
turtle.forward(root)

turtle.left(90)
turtle.forward(root* 1/2)

turtle.left(90)
turtle.forward(root* 1/2)

turtle.left(90)
turtle.forward(root)

turtle.done()
