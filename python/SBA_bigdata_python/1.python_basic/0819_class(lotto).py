# 로또 주문하는 class
# 1~10까지 주문
# 6개의 숫자로 된 로토는 오름차운으로 정렬
# 주문한 개수만큼 일련변호를 달아서 출력
# 클래스에 메소드를 최대한 활용

import random

class Lotto:
    order_num = 0   # 주문한 롯도갯수

    def __init__(self):
        # self.order_num = order_num
        print('로또생성 프로그램입니다!')
        self.num_list = []
        pass

    def order_lotto_cnt(self):
        order_num = int(input('로또 몇개 주문할가요?[1-10]'))
        self.order_num = order_num
        return self.order_num

    def random_number(self):
        self.num_list = random.sample(range(1,46), 20)
        # for i in range(6):
        #     while True:
        #         num_lotto = random.randint(1,45)
        #         if num_lotto in self.num_list:
        #             continue
        #         else:
        #             self.num_list.append(num_lotto)
        #             break
        return self.num_list

    def repeat_lotto(self):
        order_cnt = self.order_lotto_cnt()
        for i in range(order_cnt):
            lotto_list = self.random_number()
            print(i+1, lotto_list)

lotto = Lotto()
print(lotto.repeat_lotto())