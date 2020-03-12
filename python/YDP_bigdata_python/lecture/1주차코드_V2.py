# 
# Basic Codes for Operators

a = 4
b = 3

print(a + b)


if a > b:
    print('a is larger than b')




if a > b:
    print('a is larger than b')
else:
    print('b is equal or larger than a')


if a > b:
    print('a is larger than b')
elif a==b:
    print('b is equal to a')
else:
    print('b is larger than a')




gender = 'woman'
age = 21

if gender == 'man':
    if age >= 20:
        print('성인 남성')
    else:
        print('미성년자 남성')
else:
    if age >= 20:
        print('성인 여성')
    else:
        print('미성년자 여성')


a = 3
'홀수' if a % 2 == 1 else '짝수'




# Print Even numbers under 20
for i in range(1,11):
    print(i*2)


start = 1
while start <= 10:
    print(start)
    start = start + 1



def is_even(n):
    if n % 2 == 0:
        return True
    elif n % 2 == 1:
        return False

is_even(2) # True



import random

def choice_in_menu(dinner):
    choice = random.choice(['a', 'b', 'c'])
    if dinner == 1:
        if choice == 'a':
            print('차돌박이 된장찌개')
        elif choice == 'b':
            print('삼겹살')
        elif choice == 'c':
            print('제육볶음')
        else:
            print('그런 메뉴는 없습니다.')
    elif dinner == 2:
        if choice == 'a':
            print('초밥')
        elif choice == 'b':
            print('우동')
        elif choice == 'c':
            print('카레')
        else:
            print('그런 메뉴는 없습니다.')
    elif dinner == 3:
        if choice == 'a':
            print('짜장면')
        elif choice == 'b':
            print('짬뽕')
        elif choice == 'c':
            print('볶음밥')
        else:
            print('그런 메뉴는 없습니다.')
    else:
        print('그런 식단은 없습니다.')

choice_in_menu(dinner=1)

def yoon(year):
    if year%4 == 0:
        if year%400 == 0:
            print('윤년입니다.')
        elif year%100 == 0:
            print('윤년이 아닙니다.')
        else:
            print('윤년입니다.')
    else:
        print('윤년이 아닙니다.')

yoon(398)
yoon(400)
yoon(396)
yoon(300)

'''
/새롭게 추가한 부분
'''

###############
# 기본자료형
###############
# int
a = 1
type(a)

# float
a = 1.
type(a)

# complex
a = 1 + 2j
type(a)
a += 1j
a

# bool
a = True
type(a)
not a
a == 1
a == 2
not a == 0

# str
a = 'abc'
type(a)
b = 'ABC'
a + b
a * 3
# try 'abc' -> 'aBc'
try:
    a[1] = 'B' # 변경
except TypeError:
    print('str is immutable')
    # alternative
a_new = a[0] + 'B' + a[2]

###############
# list
###############
# 생성
# 1
a = [0, 1, 2, 3, 4, 5] 
# 2
a = list(range(6))
# 3
a = [] 
for i in range(6):
    a.append(i)
# 4
a = [i for i in range(6)] # is called list comprehension
# 5 
a = list('012345')
a
list(map(int, a)) # 각 원소에 int()를 적용

# 접근 & 변경
# 1
a = [0, 1, 2, 3, 4, 5]
a[0] = 100
a
a[1:2] = [1000]
a
a[1:3] = 200, 200 # a[1:3] = [200, 200]
a
a[0:6:2] = 300,300,300  # 0 2 4에 300
a

# 삽입
a = [0, 1, 2, 3, 4, 5]
a.append(6)
a
a = a + [7]
a
a = [-1] + a
a
a = a[0:3] + [200] + a[3:len(a)] # 3번째에 element 삽입 
a
a.append(range(6)) # 참고: 모든 객체를 담을 수 있다.
a

# 삭제
a = [0, 1, 2, 3, 4, 5]
a.pop(0) # 0 번째
a
del a[0] # 0 번째
a
# 참고 : del은  python 연산자
# 참참고 : 물론 객체 내에 __del__이 구현되어있어서 내부적으론 객체 내의 메소드 호출한 것)
a.pop(-1) # -1 번쨰 = 마지막
a

# 탐색
a = [0, 1, 2, 3, 4, 100]
len(a)
max(a)
min(a)
a.count(100)
a.index(100)

# 정렬
a = [0, 1000, 2, -100, 4, 100]
sorted(a)
a
a.sort() # 원본 수정
a
a = [0, 1000, 2, -100, 4, 100]
sorted(a, reverse=True) # 역순
sorted(a, key = lambda x: -x) # 역순 = -를 취한 것을 기준으로 정렬
# 참참고 : lambda는 짧은 방식으로 함수를 정의한 것
def minus(x):
    return -x
sorted(a, key = minus)

###############
# tuple
###############
# 생성
# 1
a = (0, 1, 2, 3, 4, 5)
# 2
a = tuple(range(6))
# 3
a = tuple(map(int, '0 1 2 3 4 5'.split()))

# 접근 , 변경은 불가능
# 1
a = (0, 1, 2, 3, 4, 5)
a
a[1:2] # 1 에 접근
a[1:3] # 0 1 2 에 접근
a[0:6:2] # 0 2 4에 접근

###############
# dictionary
###############

# 생성
prices = {
    'Naver' : 42.1,
    'Samsung' : 302.78,
    'LG' : 325.25,
    'Sk' : 73.10,
    'Hyundai' : 90.75
}

# 접근
prices['Naver']

# 삽입
prices['Kakao'] = 100
prices

# 삭제
del prices['Samsung']
prices

# 탐색
prices
len(prices)
max(prices) # 이름이 사전 배열에서 가장 높은 것을 고름 
max(prices, key = lambda x: prices[x]) # 값을 기준으로 고름
min(prices)
min(prices, key = lambda x: prices[x])
prices.values()
prices.keys()
max(zip(prices.keys(), prices.values()), key = lambda x: x[1]) # 이름과 함께 출력하려면, (회사이름, 가격) 으로 묶어주고 key를 가격으로 
prices.items() # key와 value를 함께 묶어준다.
max(prices.items(), key = lambda x: x[1])

# 정렬
sorted(prices) # 이름으로 나열
sorted(prices, key = lambda x: prices[x]) # 가격으로 나열 (저렴한 순)
sorted(prices, key = lambda x: -prices[x]) # 가격으로 나열 (비싼 순)
sorted(zip(prices.values(), prices.keys())) # 이름과 함께

'''
새롭게 추가한 부분/
'''






a = {'key1' :  1, 'key2' :  2}

sorted(a)
a = {'key2' :  1, 'key1' :  2}

sorted(a, reverse=True)


grades_list = [['001', 100, 90, 'A'], ['002', 10, 30, 'D'], ['003', 70, 80, 'B']]
for student in grades_list:
    if student[0] == '001':
        print(student[1:])

grades_list = {'001' : [100, 90, 'A'], '002' : [10, 30, 'D'], '003' : [70, 80, 'B']}
grades_list['001']


from operator import itemgetter

sorted(grades_list.items(), key = lambda x : x[1][2])


# 가변인수는 종종 args(arguments)라고 명명한다.
def calcsum(*args):
    return sum(args) # sum((arg1, arg2, ...))

calcsum(1, 2, 3) # 6

# 키워드 가변인수는 종종 kargs(keyword arguments)라고 명명한다.
def compute(**kargs):
    return kargs['add'] - kargs['sub'] * kargs['mul']

compute(add = 2, sub = 3, mul = 4) # -10



class Cat():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def is_overweight(self):
        if self.weight > 10:
            print('과체중')
        else:
            print('정상')

cat1 = Cat("Leon", 11)
cat2 = Cat("Nabi", 9)

print(cat1.name) # Leon
print(cat2.name) # Nabi

print(cat1.weight) # 11
print(cat2.weight) # 9

cat1.is_overweight() # 과체중
cat2.is_overweight() # 정상

cat1_name = 'Leon'
cat1_weight = 11
cat2_name = 'Nabi'
cat2_weight = 9

print(cat1_name) # Leon
print(cat2_name) # Nabi

print(cat1_weight) # 11
print(cat2_weight) # 9

def is_overweight(weight):
    if weight > 10:
        print('과체중')
    else:
        print('정상')

is_overweight(cat1_weight) # 과체중
is_overweight(cat2_weight) # 정상

class Human():
    def __init__(self, name, gender, reg_num):
        self.name = name
        self.gender = gender
        self.reg_num = reg_num # 주민등록번호
    
    def identify(self):
        print('이름 : {name}\n성별 : {gender}\n주민번호 : {reg_num}'.format(\
            name=self.name, gender=self.gender, reg_num=self.reg_num))

    def trans_name(self, new_name):
        self.name = new_name

class Student(Human):
    def __init__(self, name, gender, reg_num, student_id, major):
        super().__init__(name, gender, reg_num)
        self.student_id = student_id
        self.major = major
    
    # 오버라이딩 : 상속된 메소드를 새로 정의하고 싶다
    def identify(self):
            print('이름 : {name}\n학번 : {student_id}\n전공 : {major}'.format(\
                name=self.name, student_id=self.student_id, major=self.major))

    def trans_major(self, new_major):
        self.major = new_major

student1 = Student('홍길동', '남성', '901111-1111111', '2011111111', 'math')
student1.identify()
'''
이름 : 홍길동
학번 : 2011111111
전공 : math
'''

student1.trans_name('홍동길')
student1.identify()
'''
이름 : 홍동길
학번 : 2011111111
전공 : math
'''

student1.trans_major('computer')
student1.identify()
'''
이름 : 홍동길
학번 : 2011111111
전공 : computer
'''

class Student2(Human):
    def __init__(self, name, gender, reg_num, student_id, major):
        super().__init__(name, gender, reg_num)
        self.student_id = student_id
        self.major = major
    
    # 오버라이딩 : 상속된 메소드를 새로 정의하고 싶다
    def identify(self):
            print('이름 : {name}\n학번 : {student_id}\n전공 : {major}'.format(\
                name=self.name, student_id=self.student_id, major=self.major))

    def trans_major(self, new_major):
        self.major = new_major

    def __repr__(self):
        return '{name}\n인터프리트 모드에서 출력되는 표현식'.format(name=self.name)
    
    def __str__(self):
        return '{name}\nprint()하면 출력되는 문자열'.format(name=self.name)

    def __add__(self, other_student):
        return '{name}'.format(name=self.name + other_student.name)

student1 = Student2('홍길동', '남성', '901111-1111111', '2011111111', 'math')
student1 # __repr__ 실행
print(student1) ## __str__ 실행

student2 = Student2('홍동길', '남성', '901112-1111111', '2011111112', 'computer')
student1 + student2 # 홍길동홍동길

class Integer():
    def __init__(self, n):
        self.n = n

    def __add__(self, other):
        return self.n + other.n

n1 = Integer(1)
n2 = Integer(2)

print(n1 + n2)