import  requests
import  re #정규식
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

for i in range(1, 6): # 1페이지부터 5페이지
    print("페이지 :", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

    res = requests.get(url, headers=headers) #컴퓨터가 접근하는 것이 아닌 유저가 접근하는 것처럼 속이는 것
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})

    for item in items:
        ad_badge = item.find("span", attrs={"class":"ad-badge-text"})

        if ad_badge:
            continue #광고인부분은 그냥 넘어감

        name = item.find("div", attrs={"class":"name"}).get_text()

        if "Apple" in name: #apple제품이면 제외
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text()
        rate = item.find("em", attrs={"class": "rating"})#평점이 없는 상품도 있음.

        if rate: #값이 있으면 출력
            rate = rate.get_text()
        else: #평점 없으면 제외
            continue

        rate_cnt = item.find("span", attrs={"class": "rating-total-count"})

        if rate_cnt:  # 값이 있으면 출력
            rate_cnt = rate_cnt.get_text() #예: (26)
            rate_cnt = rate_cnt[1:-1] #()부분 지우는것 앞에 1칸 뒤에서 1칸
        else: #평점 수 없으면 제외
            continue
        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 100:
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점 ({rate_cnt}개)")
            print("바로가기 : {}".format("https://www.coupang.com" + link))
            print("-"*100) #줄긋기
