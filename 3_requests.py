import requests
url = "https://naver.com"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
Chrome/87.0.4280.141 Safari/537.36"} #나의 useragent
res = requests.get(url, headers=headers)
#res.raise_for_status() #문제가 있으면 바로 프로그램을 종료함 위에 줄이랑 같이 쓰면됨 실과 바능존래
with open("nadocoding.html", "w", encoding="utf8") as f: #f는 이름
    f.write(res.text)  #스크래핑에서 파일로 가져옴

#res = requests.get("https://nadocoding.tistory.com") #홈페이지 실행
# print("응답코드 :", res.status_code) #정상적으로 불러왔는지 확인 200이면 정상
#
#
# if res.status_code == requests.codes.ok: #200이랑 똑같은 말
#     print("정상입니다.")
# else:
#     print("문제가 생겼습니다. [에러코드", res.status_code, "]")
#
# print(len(res.text)) #페이지의 문자열 길이를 가져옴

