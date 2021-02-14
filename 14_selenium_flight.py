from  selenium import  webdriver
from  selenium.webdriver.common.by import  By
from  selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
browser = webdriver.Chrome()
browser.maximize_window() # 창최대화

url = "http://flight.naver.com/flights/"
browser.get(url) #url로 이동

browser.find_element_by_link_text("가는날 선택").click() #텍스트로 찾기

# browser.find_elements_by_link_text("27")[0].click() #elements로해서 [0] -> 이번달
# browser.find_elements_by_link_text("28")[0].click() #elements로해서 [0] -> 이번달

browser.find_elements_by_link_text("27")[0].click() #elements로해서 [1] -> 다음달
browser.find_elements_by_link_text("28")[1].click() #elements로해서 [11 -> 다음달

#제주도 선택
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

#항공권검색 클릭
browser.find_element_by_link_text("항공권 검색").click()
try:
    elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[2]/div/div[4]/ul/li[2]")))
    #튜플형태로 함 ()
finally:
     browser.quit()
#어떤 엘리먼트가 나올때까지 10초까지 기다림(인터넷이 동작을 하기까지 기다려야하는데 로딩 속도를 모르기때문에 로딩이 다 되면 알아서 실행되게함.
#xpath외에도 ID, CLASS_NAME, LINK_TEXT등 사용 가능
#첫번째 결과 출력
elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[2]")
print(elem.text)