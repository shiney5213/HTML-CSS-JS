
name = '홍길동'
greeting = '안녕'

print(name, greeting)
print(greeting, name)

text = name + '님,'+ greeting + '하세요'
print(text)


coffee1_name = '카페라떼'
coffee1_val = 4000
coffee2_name = '카푸치노'
coffee2_val = 4500
coffee3_name = '마끼야또'
coffee3_val = 5000

# case1
print('가격은'+ str(coffee1_val + coffee2_val + coffee2_val)+'입니다')

# case2
coffee_val = coffee1_val + coffee2_val + coffee3_val
print('손님, \n%s, %s, %s을 주문하셨습니다.' % (coffee1_name, coffee2_name, coffee3_name))
print('가격은 %d원입니다' % coffee_val)

