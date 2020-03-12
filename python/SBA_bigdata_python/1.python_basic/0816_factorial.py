
# 팩토리얼 표: 0~100 까지의 factorial  table
idx, gop, sum = 0, 0, 0
factorial = []
total_sum = []

# 숫자인지 문자인지 확인(하나라도 문자면 결과 값을 곱하면 0이 됨)
num_chk_list = list('01234567789')  # 문자열 리스트로 저장

while True:
    key_in = input('숫자를 입력해주세요(1~100)')
    chk_num = True
    for char in key_in:
        is_num = char in num_chk_list  # True, False값 반환
        # print('is_num:', is_num)
        chk_num *= is_num
        if not chk_num:
            break

    if chk_num :
        last_num = int(key_in)
        print('입력한 숫자:', last_num)
        break
    else:
        print('입력한 값이 숫자가 아닙니다')


# 입력한 값이 숫자인 경우, 미션 수행
title = str(last_num) + '까지의 팩토이러 테이블 구하기!!'
print('-'* 100)
print(title)
print('-'* 100)

numbers= list(range(last_num+1))  # 계산하기 수월하게 list 다시 생성

while idx < len(numbers):
    num = numbers[idx]
    gop *= num
    gop = 1 if gop<1 else gop

    factorial.append(gop)   # fatcotial의 값을 순차적으로  list에 저장
    idx += 1


for fact_num in range(len(factorial)):
    print(str(fact_num) + '! = ', factorial[fact_num])  # list에 저장한 내용을 순차적으로 출력

