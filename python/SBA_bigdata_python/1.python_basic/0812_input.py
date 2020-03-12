# 표준 입력문

# name = input('당신의 이름은 무엇입니까?')
# print(name + '님, 반갑습니다')

order = input('00카페입니다. \n무엇을 주문하겠습니까?')
count = input('몇 잔 드릴가요?')

cost = 4500 * int(count)
print('%s %s잔을 주문하셧습니다 \n 결제하실 금액은 %s입니다 '% (order, count, cost))



