import  requests
import  re #정규식
from bs4 import BeautifulSoup

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}
res = requests.get(url, headers=headers) #컴퓨터가 접근하는 것이 아닌 유저가 접근하는 것처럼 속이는 것
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

#li인데 클래스가 search-product로 시작하는 것을 찾기 위해
#re.complie을 사용하고 ^붙여준다.
items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
#print(items[0].find("div", attrs={"class":"name"}).get_text())
for item in items:

    #광고 제품은 제외
    ad_badge = item.find("span", attrs={"class":"ad-badge-text"})
    if ad_badge:
        print(" <광고 상품 제외합니다>")
        continue #광고인부분은 그냥 넘어감

    name = item.find("div", attrs={"class":"name"}).get_text()
    #애플 제품 제외
    if "Apple" in name:
        print("애플 상품 제외합니다.")
        continue
    price = item.find("strong", attrs={"class":"price-value"}).get_text()

    #리뷰 100개 이상, 평점 4.5이상 되는 것만 조회

    rate = item.find("em", attrs={"class": "rating"})#평점이 없는 상품도 있음.
    if rate: #값이 있으면 출력
        rate = rate.get_text()
    else:
        print(" <평점없는 상품 제외합니다.")
        continue

    rate_cnt = item.find("span", attrs={"class": "rating-total-count"})
    if rate_cnt:  # 값이 있으면 출력
        rate_cnt = rate_cnt.get_text() #예: (26)
        rate_cnt = rate_cnt[1:-1] #()부분 지우는것 앞에 1칸 뒤에서 1칸
    else:
        print(" <평점 수 없는 상품 제외합니다.")
        continue

    if float(rate) >= 4.5 and int(rate_cnt) >= 100:
        print(name, price, rate, rate_cnt)

