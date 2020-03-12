#case 1
text = input('영어 문장을 입력하세요')

reverse_text = str()

for x in range(len(text)-1, -1, -1):
    print(x)
    reverse_text += text[x]

print(reverse_text)


# case 2
s = 'abcde'
s_reverse = ''  # 기존 문자열을 역순으로 담아줄 빈 문자열 선언
for char in s:
    s_reverse = char + s_reverse

print(s_reverse)  # edcba


# case 3
s = 'Reverse this strings'
s2 = s[::-1]
print(s2)