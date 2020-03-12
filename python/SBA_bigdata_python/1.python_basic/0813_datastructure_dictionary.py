# 사전형 생성
bans = {'잎새반':'찬영이',
        '열매밥':'예영이',
        '햇살반':'준영이',
        '열매반':'채영이'}  # 열매반이 존재하므로, 예영이-> 채영이로 변경

print(type(bans))
print('반의 수:', len(bans)) # 열매반이 2반이르모

# 읽기
print('잎새반:', bans['잎새반'])
print('열매밥:', bans['열매반'])
print('bans 읽기',bans)

# 추가
bans['잎새반'] = '서영이'
print('bans 추가',bans)

# 변경
bans['잎새반'] = '희영이'
print('bans 변경',bans)

# 삭제
del bans['햇살반']
print('bans 삭제',bans)



# 사전형 함수
customer = {
    'name': '김진수',
    'gender': '남자',
    'email': 'bigpycraft@gmail.com',
    'company':'빅파이크래프트'
}

print('customer.keys:', customer.keys())
print('customer.values:', customer.values())
print('customer.items:', customer.items())

for key, value in customer.items():
    print('%s : %s' %(key, value))
