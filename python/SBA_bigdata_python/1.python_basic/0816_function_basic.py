# 함수 생성
def add_tex(arg1, arg2):
    print(arg1, arg2)

param1 = '대한민국'
param2 = '짝' * 5

add_tex(param1, param2)

# 함수 생성 2

def add_num (num1, num2):
    result = num1 + num2
    return result

param1 = 40
param2 = 50
sum = add_num(param1, param2)
print('%d와 %d의 합은 %d입니다' %(param1, param2, sum))


# no return function
def sayHEllo():
    print('hi, Guys!!')
    # return None : 생략되었다고 볼 수 있음.

sayHEllo()
# return 값 확인
print(sayHEllo()) # None


# 함수 호출
def exchangeUSDtoKRW (dallar):
    won = dallar * 1065
    return won

usd = 2000
krw = exchangeUSDtoKRW(usd)


# 인세를 계산하는 함수
def clac_royalty (price, sales, per):
    rate = per / 100
    royalty = int(price * sales * rate)
    return royalty

# 사용자가 정보를 입력한다
price = int(input('책의 정가는?'))
sales = int(input('발행 부수는?'))
per = int(input('인세율(퍼센트)는?'))

# 결과 표시
v = clac_royalty(price, sales, per)
print('인세는', v, '원입니다.')

# 인자값, 반환값 없는 함수
def my_func1():
    print('')
    pass


# default argment
def orderMenu(menu):
    print('손님, %s를 주문하였습니다' %(menu))

orderMenu('카페모카')

print('=' * 30)



# keyword Argument
# keyward Arguments 키워드 인자 활용하기
def introduceMyCar(brand, seats = 4, type = '세단'):
    print('나의 차는 {b} {s}인승 {t}이다'.format(b = brand, s = seats, t = type))

# 위치 인자값 1개
introduceMyCar('아우디')

# 키워드인자값 1개
introduceMyCar(brand = '렉서스')

# 키워드인자값 1개, 키워드 인자값 1개 혼용으로 사용
introduceMyCar('제규어', seats = 2)

# 순서 바뀐 키워드 인자값 2개, 순서가 바뀐 경우에는 반드시 키워드 인자값 사용
introduceMyCar(type = '미니벤', brand='카니발')

# 순서를 지킨 위치 인자값 3개: 순서가 같다면 모두 위치 안자값 사용 가능
introduceMyCar('카니발', 9,'미니벤')

# 순서 바뀐 키워드 인자값 3개,: 순서가 바뀐 경우에는 반드시 키워드 인자값 사용
introduceMyCar('쉐보리', type = 'SUV', seats = 7)



# Arbitrary Argument : 가변인자 리스트 활용
def introduceMyFamily(my_name, * family_names, **family_info):
    print('안녕하세요, 저는 %s입니다' %(my_name))
    print('*' * 35)
    print('제 가족들의 이름은 아래와 같아요')

    for name in family_names:
        print('* %s' %(name), end = '\t')
    else:  # for문이 끝나고 실행되는 무장
        print()
    print('-' * 35)

    for key in family_info.keys():
        print('- %s: %s' %(key, family_info[key]))

introduceMyFamily('진수', '희영','찬영','준영','채영',주소 = '롯데캐슬', 가훈='극기상진', 소망 = '세계일주')


####unpacking
def add(a, b):
    return a + b

data = (10, 20)
print(add(*data))

def introduce(name, greeting):
    return "{name}님, {greeting}".format(name = name, greeting = greeting)

introduce_dict = {'name': "개똥이", 'greeting':'안녕하세요'}

print(introduce(**introduce_dict))


# scope of variable
# 전역변수와 지역 변수

param = 10
strdata = '전역변수'

def func1():
    '''
    아무 것도 하지 않지만 문서만 기술한 하무
    본 함수는 docstring을 설명하기 위한 함수로 아무 행위도 하지 않는다.

    :return:
    '''
    strdata = '지역변수'
    print('func1.strdata = %s, id = %d' %(strdata, id(strdata)))

def func2():
    param = 20
    print('func2.param = %d, id = %d' %(param, id(param)))

def func3():
    global param
    param = 30
    print('func3.param = %d, id = %d' %(param, id(param)))

func1()
print('main1.strdata = %s, id = %d' %(strdata, id(strdata)))

func2()
print('main2.param = %d, id = %d' %(param, id(param)))

func3()
print('main3.param = %d, id = %d' %(param, id(param)))


print('-'* 20)


# documentation strings(docstring)
def my_function():
    """아무 것도 하지 않지만, 문서만 기술한 함수
    본 함수는 docstring을 설명하기 위한 함수로 아무 행위도 하지 않는다
    """
    pass

print(my_function.__doc__)  #""" """내의 내용 출력해줌.


# 문서화를 위한 문자열 활용
def incroduce_your_family(name, * familly_names, **family_info):
    '''
    가족을 소개하는 함수입니다.
    Args:
        name: 자기 이름 입력하기
        *family_names: 가족 이름 입력하기
        ** family_info: 가족 소개하기
    returns: 없습니다.

    :param name:
    :param familly_names:
    :param family_info:
    :return:
    '''
    pass