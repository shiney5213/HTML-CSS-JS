# 이벤트 기반 프로그래밍
# 이벤트에 따라 함수들이 호출되어 실행

#
# # turtle exam
# # 아티스트가 된 거북이(거북이 직접 움직이기)
# import turtle as t
#
# def turn_right():
#     t.setheading(0)
#     t.forward(10)
#
# def turn_up():
#     t.setheading(90)
#     t.forward(10)
#
# def turn_left():
#     t.setheading(180)
#     t.forward(10)
#
# def turn_down():
#     t.setheading(270)
#     t.forward(10)
#
# def blank():
#     t.clear()
#
#
# t.shape('turtle')
# t.speed(10)
# t.onkeypress(turn_right, "Right")  # 화살표 right를 누르면 turn_right를 호출
# t.onkeypress(turn_up, "Up")
# t.onkeypress(turn_left, "Left")
# t.onkeypress(turn_down, "Down")
# t.onkeypress(blank, "Escape")
#
# t.listen()  # 키 입력모드가 실행되어 입력된 키에 반응, 보통 코드의 끝에 위치
# t.mainloop()  # turtle.done()


import turtle as t
t.speed(1)
t.pensize(5)
t.shape('turtle')

t.onscreenclick(t.goto)
t.mainloop()

t.done()

