import turtle
import time


# # 사각형 그리기
# input('엔터를 치면 사각형을 그립니다')
#
# turtle.color("red")
# turtle.forward(200)
#
# turtle.left(90)
# turtle.forward(200)
#
# turtle.left(90)
# turtle.forward(200)
#
# turtle.left(90)
# turtle.forward(200)
#
# turtle.done()


# 사각형 그리기 응용

# size = input('사각형의 크기를 입력하세요[100~300]')
# color = input('선 색을 입력하세요[red/green/blue]')
# thick = input('펜의 굵기를 입력하세요[1~30]')
#
# angle = 90
# thick = int(thick)
# size = int(size)
#
#
# turtle.color(color)
# turtle.pensize(thick)
# turtle.shape('turtle')
#
# time.sleep(1)
# turtle.forward(size)
#
# time.sleep(1)
# turtle.left(angle)
# turtle.forward(size)
#
# time.sleep(1)
# turtle.left(angle)
# turtle.forward(size)
#
# time.sleep(1)
# turtle.left(angle)
# turtle.forward(size)
#
# time.sleep(1)
# turtle.done()



# 원 그리기
input('엔터를 치면 파란색 굵은 원을 그립니다')

turtle.right(30)
turtle.color('blue')
turtle.circle(200)

turtle.done