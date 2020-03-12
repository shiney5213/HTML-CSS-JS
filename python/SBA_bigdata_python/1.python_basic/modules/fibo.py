def fib(n):
    '''
    n까지의 피보나치 수열을 출력하는 함수
    :param n: Integer
    :return: None
    '''
    a, b = 0, 1
    while b < n:
        print(b, end='')
        a, b = b, a + b
    print()

def fib2(n):
    '''
    n까지의 피보나치 수열을 반환하는 함수
    :param n: Integer
    :return: List
    '''
    result = []
    a, b= 0, 1
    while b < n:
        result.append(b)
    return result
