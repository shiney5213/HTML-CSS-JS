# 튜플

girl_group = ('트와이스','레드벨벳','에이핑크','걸스데이','우주소녀')

print('girl_group:', girl_group)
print('girl_group[:2]:', girl_group[:2])
print('girl_group[-2:]:', girl_group[-2:])

#튜플형 변경시도 => type error
# girl_group[2] = '블랙핑크'


# 튜플형 변경
girl_group = list(girl_group)
girl_group[2] = '블랙핑크'
girl_group = tuple(girl_group)
print(girl_group)


# 튜플형 응용
width = 20
height = 30
area = width * height

print('너비', width)
print('높이', height)
print('넓이', area)
print('-'* 14)

data = (15,50)   # 값 2개를 묶을 때 사용
width, height = data   # 순차적으로 변수에 저장됨.
area = width * height


print('너비', width)
print('높이', height)
print('넓이', area)



