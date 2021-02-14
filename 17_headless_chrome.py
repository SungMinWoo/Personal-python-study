from  selenium import webdriver
#백그라운드에서 동작해서 눈에 보이진않음.
options = webdriver.ChromeOptions()
options.headless= True
options.add_argument("window-size=1920x1080")

browser = webdriver.Chrome(options=options)
browser.maximize_window()
#페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)
#지정한 위치로 스크롤 내리기
#세로 방향으로 스크롤을 1080 위치로 내리라는 말임 컴퓨터 해상도마다 다름 이건 1920x1080
#browser.execute_script("window.scrollTo(0, 1080)")

#화명가장 아래로 스크롤 내리기
#browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")

import  time
interval = 2 #2초에 한번씩 스크롤 내림

#현재문서 높이를 가져와서 저장
prev_height = browser.execute_script("return document.body.scrollHeight")

#반복수행
while True:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(interval)

    curr_height = browser.execute_script("return document.body.scrollHeight")
    if curr_height == prev_height:
        break
    prev_height= curr_height

print("스크롤 완료")
browser.get_screenshot_as_file("goole_movie.png")
import requests
from  bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")
#스크롤을 다 내린 페이지 정보를 가져옴
#movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc","Vpfmgd"]})
#리스트를 활용하여 불러올 수 있음
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    #print(title)
    #할인 전 가격
    original_price = movie.find("span", attrs={"class": "SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        #print(title, " <할인되지 않은 영화 제회>")
        continue
    #할인된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    #링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    #올바른 링크 : https://play.google.com + link

    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-"*100)

browser.quit()#브라우저 종료