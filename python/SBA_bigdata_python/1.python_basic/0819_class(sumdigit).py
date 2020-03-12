# data type에 대한 이해
# 2 ** 15 = 32768의 각 자리수를 더하면 3 + 2 + 7 + 6 + 26
# 2 ** 1000의 각 자리수를 모두 더하면 얼마입니까?

def sum_digit(num):
    num2 = str(num ** 1000)

    sum = 0
    for i in num2:
        # print(i, type(i))
        sum += int(i)
        # print(sum)
    return sum

print(sum_digit(2))
#
# num = str(2 **1000)
#
# a = []
# for i in num:
#     a.append(i)
#
#
# print(a)


