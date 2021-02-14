import  requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn" #네이버 웹툰 Url 접근
res = requests.get(url)
res.raise_for_status()#오류면 종료

soup = BeautifulSoup(res.text, "lxml")

# cartoons = soup.find_all("a", attrs={"class":"title"}) #a태그 안에있는 클래스 속성이 타이틀인 모든 값을 가져옴
# for cartoon in cartoons: #네이버 웹툰 전체 목록 가져오기
#     print(cartoon.get_text())


# rank_fors = soup.find_all("a", attrs={"class":"tit"}) #a태그 안에있는 클래스 속성이 tit인 모든 내용 가져오기
# for rank in rank_fors:
#     print(rank.get_text())