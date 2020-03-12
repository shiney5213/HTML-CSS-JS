import turtle

turtle.speed(100)
turtle.color('red')
turtle.shape('turtle')
turtle.pensize(5)


for j in range(6):
    for i in range(6):
        turtle.forward(100)
        turtle.left(60)
    turtle.forward(100)
    turtle.right(60)
# turtle.left(120)
# turtle.forward(100)
# turtle.left(60)
# turtle.forward(100)
# turtle.left(180)


turtle.done()