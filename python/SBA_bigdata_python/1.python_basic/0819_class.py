#class

# # class 이해: 문자열형 변수 var생성
# var = '파이썬, 클래스와 객체'
#
# print('var :', var)
# print('id(var) :', id(var))
# print('type(var) :', type(var))  # <class 'str'>
#
# #str, str 타입, str의 식별자 확인
# print('/nstr:' ,str)
# print('type(str:', type(str))  # <class 'type'>
# print('id(str): ',id(str))
#
# # var지역변수 __class__값 확인
# print('var.__class__:', var.__class__)  # <class 'str'>
#
#
# var2 = var.replace('파이썬', 'python')
# print(var2)

#
#
# print('-'* 20)
#
# # 클래스 정의
# # 클래스 정의 : X
# class MyClass:
#     name = '희영'
#
#     def sayHello(self):
#         hello = "Hello, " + self.name + "\t It's Good day !"
#         return hello
#
#
# myClass = MyClass()
# obj_name = myClass.name
# obj_method = myClass.sayHello()
#
# print('Object name   :', obj_name)
# print('Object method :', obj_method)
# #
# print('-'* 20)
#
## 객체 생성, 인스턴스화
# class MyClass:
#     name = str()
#
#     def sayHello(self):
#         hello = "Hello, " + self.name + "\t It's Good day !"
#         print(hello)

# 객체 생성, 인스턴스화
# myClass = MyClass()
# myClass.name = '준영'  # 인스턴스 속성값 변경
# myClass.sayHello()



# ##클래스 초기화 함수
# 클래스 초기화 함수, __init__() 재정의
# class MyClass:
#     def __init__(self, name):     # 초기화 함수 재정의
#         self.name = name
#
#     def sayHello(self):
#         hello = "Hello, " + self.name + "\t It's Good day !"
#         print(hello)
#
# # 객체 생성, 인스턴스화
# # myClass = MyClass()
# myClass = MyClass('채영')
# myClass.sayHello()


# ## 생성자와 소멸자
# class MyClass:
#     def __init__(self):  # 객체를 만들과 동시에 실행됨.
#         print('MyClass 인스턴스객체가 생성되어 메모리에 올라갑니다')
#
#     def getClassName(self):
#         return 'MyClass'
#
#     def __del__(self):
#         print('MyClass 인스턴스 객체가 메모리에서 제거됩니다')
#
# # 객체 생성
# obj = MyClass()
# obj.getClassName()
#
# print('-'* 20)
#
# # 클래스 생성과 객체 생성
#
#
# # 클래스 변수와 인스턴스 변수
# # 클래스 변수와 인스턴스 변수
# # 변수의 선언위체 따라 달라지는 유효범위
# class MyChildren:
#     school = '대학교'       # 클래스변수 country 선언
#
#     def __init__(self, name):     # 초기화 함수 재정의
#         self.name   = name        # 인스턴스 변수 name 선언
#
#     def go_to_school(self):
#         print(self.name + '이는 ' + self.school + '에 다닙니다.')
#
# # 객체 인스턴스화
# myChild  = MyChildren('희영')
# myChild1 = MyChildren('찬영')
# myChild2 = MyChildren('준영')
# myChild3 = MyChildren('채영')
#
# myChild1.school = '고등학교'  # 클래스 변수였지만, 변수에 값을 할당하면 인스턴스화 변수가 됨.
# myChild2.school = '중학교'
# myChild3.school = '초등학교'
# # 클래스함수 호출 (인스턴스 변수 name 출력)
# myChild.go_to_school()
# myChild1.go_to_school()
# myChild2.go_to_school()
# myChild3.go_to_school()
#
#
# print('='* 20)
# # 클래스 변수와 인스턴스 변수
#
###dir()클래스 내부에 있는 객체들을 확인하는 명령어
# --가 붙어있는 것은 내부 함수()
# class  MyCountry:
#     country = 'Korea'
#     __country2 = 'korea'  # 속성값 앞에 __붙이면 이름을 다르게 변경하여 출력함=> 이름 장식 기능
#
# result  = dir(MyCountry)
# print(result)
#
# # 클래스 내부 변형변수는 정의시 사용했던 변수명으로는 접근 불가능
# num = 0
# for internal_element in result:
#     num +=1
#     print(num, internal_element)


###정보 은닉, 캡슐화
# 정보은닉 Data Hiding 혹은 캡슐화 Encapsulation
# 클래스안의 변수를 핸들링(수정/호출)하기 위한 메소드를 선언하여 호출하는 방식 : get_set함수
class MyFavorite:
    __hobby = '야구'  # 내부적으로 변수명을 다르게 사용
    __drink = '맥주'

    def get_hobby(self):   # 외부에서 private 데이터 필드를 알아내거나 수정하도록 하기 위해서
        return self.__hobby

    def get_drink(self):
        return self.__drink

    def set_hobby(self, hobby):
        self.__hobby = hobby

    def set_drink(self, drink):
        self.__drink = drink

myInfo = MyFavorite()
my_hobby = myInfo.get_hobby()
my_drink = myInfo.get_drink()
print('예전엔 %s를 좋아하고, %s를 즐겨마셨어요.'%(my_hobby, my_drink))

# myInfo.__hobby = '골프'  # 해당 값이 변하지 않음.
# myInfo.__drink = '소주'   # 내부적으로 갖고 있는 값이 바뀌지 않음.
myInfo.set_hobby('골프')  # 클래스 외부에서 접근하려면 set함수 사용
myInfo.set_drink('소주')
my_hobby = myInfo.get_hobby()
my_drink = myInfo.get_drink()
print('지금은 %s를 좋아하고, %s를 즐겨마십니다.'%(my_hobby, my_drink))
#
# print('*'* 20)
# # 부모클래스, Animal
# class Animal:
#     tribe = '동물'
#     def __init__(self, name):
#         self.name = name
#
#     def getInfo(self):
#         print('나는', self.tribe,  self.name, '입니다.')
#
# # Animal의 자식클래스, Carnivore 클래스
# class Carnivore(Animal):
#     def __init__(self, name):
#         self.name = name       # 상속받은 클래스 변수, 인스턴스 변수 모두 사용 가능
#         self.tribe = '육식동물'
#
#     def favoriteFood(self):
#         print('나는 고기를 좋아합니다.')
#
# # Animal의 자식클래스, Herbivore 클래스
# class Herbivore(Animal):
#     def __init__(self, name):
#         self.name = name
#         self.tribe = '초식동물'
#
#     def favoriteFood(self):
#         print('나는 풀을 좋아합니다.')
#
# print('-' * 50, "\n[Carnivore 객체 생성]")
# tiger = Carnivore('호랑이')
# tiger.getInfo()  # 부모 class에서 상속받은 메소드
# tiger.favoriteFood()
#
# print('-' * 50, "\n[Herbivore 객체 생성]")
# rabit = Herbivore('토끼')
# rabit.getInfo()
# rabit.favoriteFood()
#
# print('*' * 20)
#
# #다형성 Polymorphism
# #  Developer 부모 클래스 선언
# class Developer:
#     def __init__(self, name):
#         self.name = name
#
#     def coding(self):
#         print('%s는 코딩을 좋아합니다.' % self.name)
#         print(self.name + ' is developer!!')
#
#
# # PythonDeveloper 자식 클래스 선언
# class PythonDeveloper(Developer):
#     def coding(self):
#         print('%s는 Python 코딩을 좋아합니다.' % self.name) # 기능을 바꾸는 것:오버라이딩
#
#
# # JavaDeveloper 자식 클래스 선언
# class JavaDeveloper(Developer):
#     def coding(self):
#         print('%s는 JAVA 코딩을 좋아합니다.' % self.name)
#
#
# # CPPDeveloper 자식 클래스 선언
# class CPPDeveloper(Developer):
#     def coding(self):
#         print('%s는 C++ 코딩을 좋아합니다.' % self.name)
#
# pDeveloper = PythonDeveloper('찬영이')
# jDeveloper = JavaDeveloper('준영이')
# cDeveloper = CPPDeveloper('채영이')
#
# pDeveloper.coding()
# jDeveloper.coding()
# cDeveloper.coding()
#
# # 동일한 함수지만, 각각의 class에서 정의된대로 사용 : 오버랑이딩 했기 때문  => 다형성
#
# print('-', * 20)
# # 게임 유닛 만들기
#
# # unit 부모 클래스 선언
# class Unit:
#     def __int__(self, name, energy, is_fly):
#         self.name = name
#         self.enrgy = energy
#         self.is_fly = is_fly
#         self.is_allive = True
#
#     def get_tribe(self):
#         print(self.name + 'is a basic tribe!!')
#
#     def get_energy(self):
#         if self.energy > 0 :
#             print(self.name)
