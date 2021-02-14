from  selenium import  webdriver
import time
browser = webdriver.Chrome("./chromedriver.exe") #경로인데 같은 경로이면 안써도됨
browser.get("http://naver.com")

elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.find_element_by_id("id").send_keys("naver_id")
browser.find_element_by_id("pw").send_keys("password")

browser.find_element_by_id("log.login").click()

time.sleep(3)

browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("my_id")

print(browser.page_source)

browser.quit()
# elem = browser.find_element_by_class_name("link_login")
#
# elem.click()
#
# browser.back() #브라우저 뒤로가기
# browser.forward() #브라우저 앞으로가기
# browser.refresh() #브라우저 새로고침
#
# elem = browser.find_element_by_id("query") #query값 가져오기
#
# from selenium.webdriver.common.keys import Keys
# #Keys값을 입력하기 위한것
# elem.send_keys("나도코딩") #검색창에 나도코딩입력
# elem.send_keys(Keys.ENTER) #검색을 위한 enter
#
# elem = browser.find_element_by_tag_name("a") #a태그에 해당하는 href정보 가져오기
# for e in elem:
#     e.get_attribute("href")
#
# browser.get("httpL//daum.net")
# elem = browser.find_element_by_name("q")
# elem.send_keys("나도코딩")
# elem = browser.find_element_by_xpath("//*[@id='daumSearch']/fieldset/div/div/button[2]")
# #xpath 정보를 받아와서 검색버튼누르기
# elem.click() #클릭


