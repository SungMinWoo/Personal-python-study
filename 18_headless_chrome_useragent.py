from  selenium import webdriver
#백그라운드에서 동작해서 눈에 보이진않음.
#headless크롬을 쓰려면 유저에이전트 값을 바꿔줘야함.
#유저 에이전트 설정을 안해주면 headlesschrome이라고 유저 에이전트가 뜸
#사이트에서 headlesschrome이면 접속을 막을 수 있음.
options = webdriver.ChromeOptions()
options.headless= True
options.add_argument("window-size=1920x1080")
options.add_argument("User-agent=Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

dectected_value = browser.find_element_by_id("detected_value")
print(dectected_value.text)
browser.quit()