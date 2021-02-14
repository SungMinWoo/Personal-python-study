import  requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/list.nhn?titleId=675554" #네이버 웹툰 Url 접근
res = requests.get(url)
res.raise_for_status()#오류면 종료

soup = BeautifulSoup(res.text, "lxml")

gauss = soup.find_all("td", attrs={"class":"title"})
# print(gauss[0].a.get_text())
# link = gauss[0].a["href"] #링크 가져오기
# print("https://comic.naver.com" + link)


# for gauss_s in gauss: #만화제목 링크 가져오기
#     title = gauss_s.a.get_text()
#     link = "https://comic.naver.com" + gauss_s.a["href"]
#     print(title, link)

#평점가져오기
total_rates = 0
cartoons = soup.find_all("div", attrs={"class":"rating_type"})
for cartoon in cartoons:
    rate = cartoon.find("strong").get_text()
    print(rate)
    total_rates = total_rates + float(rate)
print("토탈 점수는 : {0}".format(total_rates / len(cartoons)))