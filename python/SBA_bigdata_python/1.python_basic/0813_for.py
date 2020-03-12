# range 함수
print('range(10):', list(range(10)))
print('range(5,10):', list(range(5,10)))
print('range(1,10,2):', list(range(1,10,2)))


# for문
scope = [1,2,3,4,5]
for x in scope:
    print(x)

scope = list('abcde')
for x in scope:
    print(x)


# for 문을 element를 받아서 사용하는 경우와 element개수 만큼 index를 받아서 처리하는 경우
# case 0
bts_members = ['RM','슈가','진','제이홉','지민','뷔','정국']
num = 0

for member in bts_members:
    num += 1
    print('멤버%d====>%s  \t(이름 길이 : %d)' %(num, member, len(member)))

#case 2
size = len(bts_members)

for idx in range(size):
    print('멤버%d===> %s  \t(이름길이: %d)'%(idx + 1, bts_members[idx], len(bts_members[idx])))


# draw tiangle with format

# 삼각형1
for i in range(1, 10, 2):
    mark = '*' * i
    print(mark)

# 삼각형2
for i in range(1, 10, 2):
    mark = ' ' * int((10-i)/2) + '*' * i
    print(mark)



# nested for
# 중첩 for 문
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

for x in range(3):
    for y in range(3):
        print('matrix[%d][%d]: '%(x, y), matrix[x][y], end='\t')
    else:
        print('')




# break ws continue vs pass

scope = list(range(1, 100))

for num in scope:
    if num<= 10:
        if num%2 == 0:
            pass
            print(num, 'is even number')
        else:
            continue
            print(num, 'is odd number')
    else:
        print(num, 'is bigger than ten')
        break
        print('after break')

print('프로그램을 종료합니다')
