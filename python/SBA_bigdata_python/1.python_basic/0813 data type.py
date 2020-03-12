# 논리형

x = 4
y = 9


print("x == y", x == y)
print('x !=y', x !=y)

print('x<y', x<y)
print('x>y', x>y)

print('int(True)=', int(True)) # 1
print('int(False=)', int(False)) # 0

print(True or False)  # True

print('x or y', x or y)  #4
print('x and y', x and y)  #9
print('not x', not x) # False


# is, is not
print(1 == 1.0)  # True
print( 1 is 1.0)   # False
print( 1 is not 1.0)  # True


# 형 변환
num_data = 350
str_data = '350'

sum = int(str_data)+ num_data
print('합계는?', str(sum))



# 문자열

test = '파이썬 프로그래밍 재미있다!'

result = test.startswith('파이썬')
print(result)
result = test.endswith('!')
print(result)
result = test.endswith('어려워요!')
print(result)

result = test.replace('파이선','python')
print(result)


test = 'Python Progrmming is Interesting!'
result = test.upper()
print(result)
result = test.lower()
print(result)
result = '/'.join(test)
print(result)