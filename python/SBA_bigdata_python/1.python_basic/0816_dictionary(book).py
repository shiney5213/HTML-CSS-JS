# 도서 목록 입력 및 출력
books = list()      # 책 목록 선언

# 책 목록 만들기
books.append({'제목':'파이썬 프로그램', '출판연도':'2016', '출판사':'A', '쪽수':200, '추천유무':False})
books.append({'제목':'플랫폼 비즈니스', '출판연도':'2013', '출판사':'B', '쪽수':584, '추천유무':True})
books.append({'제목':'빅데이터 마케팅', '출판연도':'2014', '출판사':'A', '쪽수':296, '추천유무':True})
books.append({'제목':'외식경영 전문가', '출판연도':'2010', '출판사':'B', '쪽수':526, '추천유무':False})
books.append({'제목':'십억만 벌어보자', '출판연도':'2013', '출판사':'A', '쪽수':248, '추천유무':True})

for book in books:  # 책 한 권씩 꺼내기 위한 루프 선언
    print(book)     # 책 한 권 데이터 출력

print('-' * 10)
many_page = []  # list()
recommends = []
all_page = 0    #int()
pub_company = set('')  # 빈 set 생성

for book in books:
    all_page += book['쪽수']   # 딕셔너리명['key'] : 값에 접근 가능 (순서가 중요하지 않기 때문에 index 사용x)
    pub_company.add(book['출판사']) # set 원소 추가
    if int(book['쪽수'] )>= 250:
        many_page.append(book['제목'])
    if book['추천유무']  :    # if 뒤에는 논리값.-> ==True 쓸 필요 없음.
        recommends.append(book['제목'])


print('쪽수가 250쪽 넘는 책 리스트:',many_page)
print('내가 추천하는 책 리스트:',recommends)
print('내가 읽은 책 전체 쪽수:',all_page)
print('내가 읽은 책의 출판사 목로:',pub_company)

# python스러운 코드
# many_page =[book['제목'] for book in books if book['쪽수'] > 250]
# recommends =[book['제목'] for book in books if book['추천유무'] ]
# pub_company ={ book['쪽수'] for book in books }
# all_page =sum([ book['쪽수'] for book in books ])
#print( 'pub_company =', sorted(pub_company))
