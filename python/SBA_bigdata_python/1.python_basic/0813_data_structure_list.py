# list
print('list==========================')

bts_members = ['RM','슈가','진','제이홉','지민','뷔','정국']

# 변수의 탑 확인
print('멤버:', bts_members)
print('tyoe:,',type(bts_members))
print('size',len(bts_members))

print(bts_members[0])
print(bts_members[1])
print(bts_members[2])
print(bts_members[3])


print('역순 출력')
print(bts_members[-1])
print(bts_members[-2])
print(bts_members[-3])
print(bts_members[-4])


# 추가/삭제
sistar_members = ['효린','소유']
print('씨스타 \t:', sistar_members)

sistar_members.append('다솜')
print('append \t:', sistar_members)

sistar_members.insert(1, '보라')
print('insert \t:', sistar_members)

sistar_members.remove('소유')
print('remove \t:', sistar_members)

pickup = sistar_members.pop(0)
print('pop:', sistar_members, end='------->')
print(pickup)

# 리스트 슬라이싱
print('리스트 슬라이싱====================================')
rainbow = ['빨강','주황','노랑','초록','파랑','남색', '보라']
print('\n무지개색깔\t:', rainbow)

print('rainbow[2:5]:', rainbow[2:5])
print('rainbow[:3]:', rainbow[:3])
print('rainbow[:]:', rainbow[:])
print('rainbow[::2]:', rainbow[::2])
print('rainbow[-3:]:', rainbow[-3:])
print('rainbow[::-1]:', rainbow[::-1])


# 리스트 응용
print('리스트 응용===============================')
solarsys = ['태양','수성','금성', '지구','화성','목성','토성','천왕성','해왕성','지구']
print('태양계:', solarsys)

# 리스트에서 특정 요소의 위치 구하기(index)
planet = '지구'
pos = solarsys.index(planet)   # 첫번째 index 찾기
print('%s 행성은 태양계에서 %d번째 위치하고 있습니다' %(planet, pos))
pos = solarsys.index(planet, 5)        # 인텍스 5번부터 찾아라-> 제일 마지막에 있는 인덱스 찾도록
print('%s 행성은 태양계에서 %d번째 위치하고 있습니다' %(planet, pos))

# 리스트에서 특정 위치의 요소를 변경하기
solarsys.pop(-1)
print('태양계:', solarsys)

planet = '화성'
pos = solarsys.index(planet)
solarsys[pos]= 'Mars'
print('태양계:', solarsys)

# 리스트에서 특정 구간에 있는 요소 추출하기
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
rock_planets = solarsys[1:5]
gas_planets = solarsys[5:]

print('암석형 행성:', end=''); print(rock_planets)
print('가스형 행성:', end=''); print(gas_planets)

# 리트스의 특정 위치에 요소 삽입하기(insert)
solarsys = ['태양','수성','금성','지구','화성','목성','토성','천왕성','해왕성']
pos = solarsys.index('목성')
solarsys.insert(pos, '소행성')
print('태양계:', solarsys)




#중첩리스트
print('중첩리스트=====================================')
city = [['서울','도쿄','베이징'],
        [ '런던','파리','로마'],
        [ '워싱턴','시카고','잭슨빌']]

print('city        :',city)
print('city[0]     :',city[0])
print('city[1]     :',city[1])
print('city[-1]    :',city[-1])
print('city[0][0]  :',city[0][0])
print('city[0][1]  :',city[0][1])
print('city[0][2]  :',city[0][2])
print('city[1][1]  :',city[1][1])
print('city[2][0]  :',city[2][0])

#
