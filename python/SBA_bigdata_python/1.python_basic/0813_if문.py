#조건값: 비교연산자

condition = False
condition = True

if condition:
    print('조건을 충족함, condition met')
if not condition:
    print('조건 충족 못함, condition not met')


# if else
num_a = 100
num_b = 200

if num_a > num_b:
    print('숫자 A가 숫자 B보다 더 큰 수 입니다')
else:
    print('숫자 A는 숫자 B와 같거나 더 낮은수 입니다')

# if_elif_else
num_a = 100
num_b = 200

if num_a > num_b:
    print('숫자 A가 더 큰 숫자입니다')
    max = num_a
elif num_a < num_b:
    print('숫자 B가 더 큰 숫자입니다')
    max = num_b
else:
    print('숫자 A와 숫자 B는 같습니다')

print('숫자 A와 숫자 B 중 최대값은 ', max, '입니다')


# 논리값: 논리연산자
#if-else문
signal_color = input('색을 영문으로 나타내어 보세요')

if signal_color == 'blue':
    print('신호등은 파란색입니다, 건나가주세요')
else:
    print('신호등은 빨간색입니다. 기다려주세요')

# if-elif -else
signal_color = input('색을 영문으로 나카내어 보세요(blue/red)')

if signal_color == 'blue':
    print('신호등은 파란색입니다, 건나가 주세요')
elif signal_color == 'red':
    print('신호등은 빨간색입니다. 건나가주세요')
else:
    print('잘못된 색입니다')

# nested if문
print('-' * 14)
signal_color = input('색을 영문으로 나타내세요')

if signal_color == 'blue':
    print('신호등은 파란색입니다. 건나가 주세요')
    is_pass = input('건널 준비가 되셨나요 [yes/no]')

    if is_pass == 'yes':
        print('네, 건너가겠습니다')
    else:
        print('다음번에 건너겠습니다')
elif signal_color == 'red':
    print('신호등은 빨간색 입니다. 기다려주세요')
else:
    print('잘못된 색입니다')



#BMI판정 프로그렘
print('BMI=========================')
weight = float(input('체중(kg)은?'))
height = float(input('신장(cm)은?'))

#BMI계산
height = height/100 # m로 고치기
bmi = weight / (height * height)

# 결과로 분기
result = ""
if bmi < 18.5:
    result = "마름"
if (18.5 <= bmi) and (bmi < 25):
    result = "보통"
if (25 <= bmi) and (bmi < 30):
    result = "가벼운 비만"
if bmi >= 30:
    result = "심한 비만"

# 결과 표시
print('-'*50)
print("BMI :", bmi)
print("판정:", result)


# 응용 : 입장료 계산 프로그램
# case 1
year = int(input('서기 몇년?'))

# 윤년 판정
is_leap = False
if year% 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            is_leap = True
        else :
            is_leap = False
    else:
        is_leap = True
else:
    is_leap = False

# 결과 표시
if is_leap :
    print('윤년입니다')
else:
    print('윤년이 아닙니다')

# case 2
# elif를 사용하는 경우: 위에서부터 조건을 차례로 검사하여 해당하는 분기 1개에만 실행이 되기 때문ㅇ
# 400 -> 100 -> 4 순으로 분기해야 함.

year = int(input('서기 몇 년?'))

is_leap = False
if year % 400 == 0:
    is_leap = True
elif year % 100 == 0:
    is_leap = False
elif year % 4 == 0:
    is_leap = True
else:
    is_leap = False

if is_leap:
    print('윤년입니다')
else:
    print('윤년이 아닙니다')


# case 3

year = int(input('서기 몇 년?'))

is_leap = (year % 400 == 0) or ((year % 100 != 0) and ( year % 4 == 0))

# 결과표시

if is_leap:
    print('윤년입니다')
else:
    print('윤년이 아닙니다')


# tutle 응용
import turtle

in_color =  input('선의 색을 지정해주세요[r, g, b, etc] ')
is_filled = input('원의 색을 채우겠습니가?[yse,/no]')

if in_color == 'R' or in_color == 'r':
    color = 'red'
elif in_color == 'G' or in_color == 'g':
    color = 'green'
elif in_color == 'B' or in_color == 'b':
    color = 'blue'
else:
    color = 'black'

turtle.begin_fill()  # 색 채우기 시작
turtle.pensize(10)
turtle.circle(100)

if is_filled == 'Y' or is_filled == 'y':
    turtle.end_fill()  # 색 체우기를 완료
else:
    pass

turtle.done()



