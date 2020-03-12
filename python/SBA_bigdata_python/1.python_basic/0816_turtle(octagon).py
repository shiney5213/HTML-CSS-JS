# 패턴: 각도, 길이 굵기, 생상
import turtle


turtle.speed(100)

colors = ['red','green','blue','yellow','purple','cyan','magenta','violet']


for i in range(45):
    turtle.forward( i*2)
    turtle.color(colors[(i+1) % 8 ])
    turtle.pensize(((i // 8) + 1)* 3 )
    turtle.left(45)


turtle.done()
