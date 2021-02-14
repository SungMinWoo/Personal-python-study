import re #정규식 라이브러리
p = re.compile("ca.e") #p = 패턴 어떤 정규식을 컴파일을 할지 결정정,
#m = p.match("case") #ca.e랑 매칭이됨
#print(m.group()) #매치되지 않으면 에러 발생
def print_match(m):
    if m:
        print("m.group():", m.group()) #일치하는 문자열 반환
        print("m.string:", m.string) #입력받은 문자열 함수가 아니라 변수라 ()가 없음.
        print("m.start():", m.start()) #일치하는 문자열의 시작 index
        print("m.end()", m.end()) #일치하는 문자열의 끝 index
        print("m.span()", m.span(), "\n") #일치하는 문자열의 시작 / 끝 index
    else:
        print("매칭되지 않음")

m = p.match("care less") #match : 문자 앞부분만 같다면 일치한다고 나옴 뒷부분less는 신경쓰지않음.
print_match(m) #care 출력

m = p.search("good care")#search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m) #care 출력

lst = p.findall("good care cafe") #findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst) # ['care', 'cafe'] 출력





# 정규식을 쓸때
# 1. p = re.compile("원하는 형태")
# 2. m = p.match("비교할 문자열") : 주어진 문자열의 처음부터 일치하는지 확인
# 3. m = p.search("비교할 문자열") : 주어진 문자열 중에 일치하는게 있는지 확인
# 4. lst = p.findall("비교할 문자열") : 일치하는 모든 것을 "리스트" 형태로 반환
#
# 원하는 형태 : 정규식
# . (ca.e) : 하나의 문자를 의미 > care, cafe, case와 같은 문자를 검색
# ^ (^de): 문자열의 시작을 의미 > desk, destination와 같은 문자를 검색
# $ (se$) : 문자열의 끝 > case, base와 같은 문자를 검색