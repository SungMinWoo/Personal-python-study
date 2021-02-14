import  csv
import  requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page="

filename = "시가총액1-200.csv"
f = open(filename, "w", encoding="utf-8-sig", newline="") #newline을 안쓰면 파일에 입력할때 한줄쓰고 엔터를 침
#엑셀 파일에서 한글이 깨질때 = utf-8-sig 넣으면됨
writer = csv.writer(f)

title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
#.split("\t")을 사용하면 tap으로 구분되어있는 것을 리스트 형태로 변환해줌
writer.writerow(title)
for page in range(1,5):
    res = requests.get(url + str(page))
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

    for row in data_rows:
        columns = row.find_all("td")
        if len(columns) <= 1: #의미 없는 데이터 스킵
            continue
        data = [column.get_text().strip() for column in columns] #한줄 for문 각 td가 가지고 있는 텍스트 정보
        #strip함수 불필요한 공백을 삭제하는 함수.
        #print(data)
        writer.writerow(data) #리스트인 data를 입력
