# immutable

hello = '안녕하세요'

print(hello)
print(id(hello))

hello = '반갑습니다'

print(hello)
print(id(hello))


# mutable
hello_list = ['안녕하세요']

print(hello_list)
print(id(hello_list))

hello_list[0] = ['반갑습니다']  # 첫번째 항목의 값 변경

print(hello_list)
print(hello_list[0])
print(id(hello_list))
print(id(hello_list[0]))