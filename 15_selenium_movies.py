import requests
from  bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36",
    "Accept-Language":"ko-KR,ko" #그냥 requests로 들어가면 외국 서버로 감 한국서버로 가게해주는코드
}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
print(len(movies))
# with open("mobie.html", "w", encoding="utf8") as f:
#     #f.write(res.text) #text형태로 출력
#     f.write(soup.prettify())#html문서를 정돈된 형태로 출력

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)