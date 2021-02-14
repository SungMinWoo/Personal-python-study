import requests
from bs4 import BeautifulSoup


for year in range(2015, 2020): #2015년부터 2020년도 영화 5순위
    url = "https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={}%EB%85%84+%EC%98%81%ED%99%94+%EC%88%9C%EC%9C%84".format(year)
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    images = soup.find_all("img", attrs={"class": "thumb_img"})

    for idx, image in enumerate(images): #tuple형태로 변환되어 idx(key)가 0,1,2,3~올라감
        image_url = image["src"]
        if image_url.startswith("//"): #//로 시작한다면 앞쪽에 https:를 붙혀주는 코드
            image_url = "https:" + image_url

        print(image_url)
        image_res = requests.get(image_url) #직접 접속해서 파일로 저장하기 위해 url선언
        image_res.raise_for_status()

        with open("movie_{}_{}.jpg".format(year,idx + 1), "wb")as f: #영화 데이터는 텍스트가 아니라 바이너리라서 wb로 씀
            f.write(image_res.content)
        if idx >= 4: #상위 5개 이미지만 다운
            break