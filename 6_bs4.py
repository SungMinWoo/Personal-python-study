import  requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn" #네이버 웹툰
res = requests.get(url)
res.raise_for_status()#오류면 종료

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title) #title 출력
# print(soup.title.get_text()) #title의 텍스트만 출력
# print(soup.a) #html에서 맨 처음 나오는 a태그를 출력
# print(soup.a.attrs) #a태그를 딕셔너리형태로 속성정보를 출력
# print(soup.a["href"]) #href의 값만 출력
# #attrs = 속성
# print(soup.find("a", attrs={"class":"Nbtn_upload"}))
# #a태그가 해당하는 첫번째 엘리먼트 중에서 class이름이 Nbtn_upload인 것을 찾을 때
# print(soup.find(attrs={"class":"Nbtn_upload"})) #a태그가 없이 사용가능

# print(soup.find("li", attrs={"class":"rank01"}))

#rank1 = soup.find("li", attrs={"class":"rank01"})
# print(rank1.a["title"]) #네이버 웹툰의 랭크 1위인 타이틀 정보

# print(rank1.a.get_text())
# print(rank1.next_sibling) #다음 형제 관계 있는 것을 가져오기
# print(rank1.next_sibling.next_sibling)
# rank2 = rank1.next_sibling.next_sibling

# rank3 = rank2.next_sibling.next_sibling
# rank2 = rank3.prevous_sibling
# print(rank1.parent) #부모로 가는 것

# rank2 = rank1.find_next_sibling("li") #li에 해당하는 태그 중 다음 것으로 넘어감
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li") #li에 해당하는 태그 중 다음 것으로 넘어감
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

#print(rank1.find_next_siblings("li")) #형제들을 모두 가져옴

webtoon = soup.find("a", text="웹툰이름") #웹툰이름이 포함된 a태그를 가져옴