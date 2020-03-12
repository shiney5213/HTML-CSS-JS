#while문
idx = 0

while idx < 5:
    print(idx)
    idx += 1

print('프로그램 종료!')


# while- ex 2
num, sum = 1, 0

while True:
    sum += num
    if sum > 100:
        break
    else:
        num += 1

print('num  값이 %d 일 때 while문 탈출' % num)


# while-ex3
numbers = [0,1,2,3,4,5,6,7,8,9]
idx, sum = 0, 0

while idx < len(numbers):
    num = numbers[idx]
    sum += idx
    idx += 1

print('numbers의 합계는', sum, '입니다')


# 신호등 문제
sigmal_color = ''
while sigmal_color != 'blue' and sigmal_color != 'red':
    sigmal_color = input('색을 영문으로 입력하세요(blue/red):')

    if sigmal_color == 'blue':
        print('신호등은 파란색입니다, 길을 건너가세요')
    elif sigmal_color == 'red':
        print('신호등은 빨간색입니다, 기다리세요')
    else:
        print('잘못된 색입니다. 다시 입력해주세요')

print('프로그램을 종료합니다')

