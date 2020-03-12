# 구구단

dan = int(input('구구단을 입력하세요[2~9]'))
print(dan,'단 출력')


#case 1
for i in range(1, 10):
    print(dan, 'x',i,'=',dan * i)




#case 2
for i in range(1, 10):
    print({0}, '*' ,{1} , '=', {2}.format(dan, i, dan))