# set

# set형 집합 연산자
a = set('abracadabra')
b = set('alacazam')

print('집합 a =', a)
print('집합 b =', b)
print('합집합 a | b =',a | b)
print('교집합 a & b =', a & b)
print('차집합 a - b =', a - b)
print('여집합, a ^ b =', a ^ b)


# 중복 제거 및 정렬
beast = ['lion','tiger','wolf','tiger','lion','bear','lion']
print('beast =', beast)

unique_beast = list(set(beast))
print('unique_beast=', unique_beast)
sorted_beast = sorted(unique_beast)
print('sorted_beast=', sorted_beast)

print(unique_beast.sort)

