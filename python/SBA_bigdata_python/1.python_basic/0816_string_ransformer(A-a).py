text = input('영어 대소문자로 이루어진 문장을 입력하세요')

print(text)

print('대문자로 변환:', text.upper())
print('소문자로 변환:', text.lower())

new_text = str()  # 신규 문자열형 변수 선언

for i in text:
    if i.islower():
        new_text += i.upper()

    else:
        new_text += i.lower()


print('대소문자 바꿔서 출력: \n' + new_text)

print('대소문자 바꿔서 출력:\n', text.swapcase() )

