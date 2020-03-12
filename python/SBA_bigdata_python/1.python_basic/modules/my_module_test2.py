# File name: my_module_test2.py

def func(a):
    print("입력 숫자:",a)

    
# 바깥에 있는 함수 이름이 __nam__
if __name__ == "__main__":
    print("모듈을 직접 실행")
    func(3)
    func(4)
