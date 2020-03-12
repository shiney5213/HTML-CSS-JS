import turtle

var1 = input('변의 수를 입력해주세요[3-8]')
var2 = input('한 변의 길이를 입력해주세요[100-200]')

var1 = int(var1)
var2 = int(var2)

color = ['red','green','blue']

angle = 360 / var1


turtle.color(color[var1 % 3])
turtle.begin_fill()
for i in range(var1):
    turtle.forward(var2)
    turtle.left(angle)

turtle.end_fill()

turtle.done()