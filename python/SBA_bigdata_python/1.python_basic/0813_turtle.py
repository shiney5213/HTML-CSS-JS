import turtle as t


# # 여러개 원 그리기
# num_circle = 30
# radius = 180
#
# t.bgcolor("blue")
# t.color('yellow')
# t.speed(0)
#
# for _ in range(num_circle):
#     t.circle(radius)
#     t.left(360 / num_circle)
#
# t.done()  # 화면을 닫지 않도록 하기

# #점선 그리기
# t.pensize(3)
# t.color('red')
#
# for i in range(10):
#     t.forward(15)
#     t.penup()
#     t.forward(15)
#     t.pendown()
#
# t.done()
#
# # 입력받아 다각형 그리기
# print('다각형을 그리는 예제입니다')
# var1 = input('변의 수를 입력해주세요[3-8]')
# var2 = input('한 변의 길이를 입력해주세요[100-200]')
#
# num_of_side = int(var1)
# len_of_side = int(var2)
#
# angle = 360.0 / num_of_side
# c_mod = num_of_side % 3 # 나머지값에 따라 색을 설정하기 위해
# color = 'red' if c_mod== 0 else 'green' if c_mod==1 else 'blue'
#
# t.begin_fill()
# t.color(color)
# t.pensize(5)
#
# for i in range(num_of_side):
#     t.forward(len_of_side)
#     t.left(angle)
#
# t.end_fill()
#
# t.done()

#turtle-nasted for문(점찍는 거북이)
# import turtle
# t = turtle.Turtle()
# t.shape('turtle')
#
# dot_distance = 50
# width = 5
# height = 4
#
# t.penup()
# for y in range(height):
#     for i in range(width):
#         t.dot()  # 점 찍기
#         t.forward(dot_distance)
#     t.backward(dot_distance * width)
#     t.right(90)
#     t.forward(dot_distance)
#     t.left(90)
#
# turtle.done()

# 거북이 키보드로 컨드롤하기
import turtle as t

print('거북이를 키보드로 움직여 보아요')
print('\tA: 왼쪽으로 이동')
print('\tD: 오른쪽으로 이동')
print('\tW: 위쪽으로 이동')
print('\tS: 아래쪽으로 이동')
print('\tX: 프로그램 종료')

input('엔터키를 누르면 시작합니다')
t.shape('turtle')
t.pensize(5)
# t.color('green')
t.speed(10)

t.begin_fill()
while True:
    direction = input('[A,S,D,F]:')
    if 'X' == direction.upper():
        break
    elif 'D' == direction.upper():
        t.color('red')
        t.setheading(0)
    elif 'W' == direction.upper():
        t.color('green')
        t.setheading(90)
    elif 'A' == direction.upper():
        t.color('blue')
        t.setheading(180)
    elif 'S' == direction.upper():
        t.color('black')
        t.setheading(270)
    else:
        continue

    t.forward(50)

t.end_fill()
print('\n프로그램을 종료하였습니다')
t.done()