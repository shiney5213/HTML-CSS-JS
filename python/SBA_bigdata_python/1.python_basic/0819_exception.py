#try_except 구분으로 예외상황 제어, Exceptions Handling in Program
# try:
#     print('안녕하세요')
#     print('param')
# except:   # 예외가 발생하지 않으면 실행되지 x
#     print('예외가 발생했습니다')



# try:
#     print('안녕하세요')
#     print(param)
# except:
#     print('예외가 발생했습니다')  # 예외 상황이 발생하면 실행
# else:
#     print('예외가 발생하지 않았습니다') # 예외상황이 발생하지 않으면 실행
# finally:
#     print('무조건 실행하는 코드') # 반드시 실행(예외 상황과 상관없이)
#
#
# try:
#     print(param)
# except Exception as e:  # 오류를 처리해주는 객체
#     print(e)   # log파일에 남기기(시간정보, 어떤 모듈, 어떤 오류)-> 오류 분석할 때 사용
#


#
# import time
# count = 1
# try:
#     while True:
#         print(count)
#         count += 1
#         time.sleep(0.5)
# except KeyboardInterrupt:  #ctrl _c가 입력되면 발생하는 오류
#     print('사용자에 의해 프로그램이 중단되었습니다')

###try-except 구문으로 예외상황 제어, Exceptions Handling in Function

###예외상황 테스트를 위한 함수
### 예외상황 테스트를 위한 함수
# def exception_test():
#     print("[1] Can you add 2 and '2' in python? ")
#     print("[2] Try it~! ", 2 + '2')  # 예외 발생
#     print("[3] It's not possible to add integer and string together. ")
#
#
# exception_test()
#
# ###예외상황에 대한 처리를 구현한 함수
# # 예외상황에 대한 처리를 구현한 함수





def exception_test2():
    print("[1] Can you add 2 and '2' in python? ")

    try:
        print("[2] Try it~! ", 2 + '2')  # TypeError 발생
    except TypeError:
        print("[2] I got TypeError! ")  # 에러 메시지 출력

    print("[3] It's not possible to add integer and string together. ")


exception_test2()


### 예외상황에 대한 에러메시지를 상세히 나타낸 함수
# def exception_test3():
#     print("[1] Can you add 2 and '2' in python? ")
#
#     try:
#         print("[2] Try it~! ", 2 + '2')  # TypeError 발생
#     except TypeError as err:
#         print("[2] TypeError: {}".format(err))  # 에러 메시지 출력
#
#     print("[3] It's not possible to add integer and string together. ")
#
#
# exception_test3()


# import traceback
#
# # 처음에 보았던 트레이스백 메시지와 함께 나타낸 함수
# def exceptiion_test4():
#     print("[1] Can you add 2 and '2' in python?")
#
#     try:
#         print("[2] Try it~!", 2 + '2')  # typeError 발생
#     except TypeError:
#         print('[2] I got TypeError! Check below!')  # errer 메시지 출력
#         traceback.print_exc()   # traceback 메시지 얻기, 에러스택 정보를 stdout으로 print
#         # except 내부에서 사용하게 될 경우 error의 발생 위치를 추적할 수 있는 call stack을 출력해줌.
#     print("[3] It's not possible to add integer and string together.")
#
# exceptiion_test4()
#
#
# # except 여러개 사용 가능
# try:
#     print(3 + '4')
# except NameError:   # 위에서 부터 순차적으로 오류 검증
#     print('파라미터 미정의')
# except TypeError:
#     print('데이터 타입 오류')
# except Exception as e:
#     print(e)    # log 파일에 남긴 후, 그 기록을 보고 나중이 오류 처리하기.
# print('프로그램 종료')

 ###예외처리 방식에서의 else 옵션 구문 활용

#
#
# def exception_test5(file_path):
#     try:
#         f = open(file_path, 'r')  # 파일 열기 시도
#     except IOError:
#         print('cannot open', file_path)  # 에러 메시지 출력
#     else:
#         print('File has', len(f.readlines()), 'lines')  # 파일 라인 수 출력
#         f.close()  # 파일 닫기
#
#
# # 정상 상황
# exception_test5('README.txt')  #File has 3 lines
#
#
# # 없는 파일을 찾을때
# exception_test5('README-XXX.txt')  #File has 3 lines


###예외 처리 방식에서의 finally옵션 구문 활용

def exception_test6(file_path):
    try:
        f = open(file_path, 'r')  # 파일 열기 시도
    except IOError:
        print('cannot open', file_path)  # 에러 메시지 출력
    else:
        print('File has', len(f.readlines()), 'lines')  # 파일 라인 수 출력
        f.close()  # 파일 닫기
    finally:
        # 예외 발생 상관 없이 무조건 실행
        print('I just tried to read this file.', file_path)


# 정상 상황
exception_test6('README.txt')
#File has 3 lines
# I just tried to read this file. README.txt

# 없는 파일을 찾을때
exception_test6('README-XXX.txt')
#cannot open README-XXX.txt
# I just tried to read this file. README-XXX.txt



#exception을 사용자 정의 함수 만들기
# raise TooBigNumError(15) 내가 만들 오류
# class TooBigNumError(Exception):   # 이미 정의된 class 상속 받기
#     def __init__(self, val):
#         self.val = val
#     def __str__(self):  # 오류가 발생했을 때 오류 내용을 뿌려주는 내부 함수
#         return 'too big number {}. Use 1~10! '.format(self.val)
#
# # raise TooBigNumError(15) # 강제로 오류 발생
#
#
# # 사용자 정의 예외를 위한 테스트 함수
# def user_difined_exception_test():
#     num = int(input('1부터 10사이의 점수를 입력하세요!'))
#     if num > 10:
#         raise TooBigNumError(num)
#     print('숫자{}를 입력하셨군요!'.format(num))
#
# # 정상 Case입력
# user_difined_exception_test()





