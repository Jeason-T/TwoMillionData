from selenium import webdriver
import time      #用来使程序运行歇息一会儿

#模拟登录百度
url = 'https://www.baidu.com'
driver = webdriver.Chrome(r'C:\Users\15872\Desktop\chromedriver.exe')
driver.maximize_window()#最大化窗口
driver.get(url)

# 找到登录按钮并点击
# login = driver.find_element_by_id('u1').find_elements_by_class_name("lb")[0]
# login.click()

login = driver.find_elements_by_css_selector("div[id=u1] a[class=lb]")[0]
login.click()
time.sleep(3)

#找到用户名登录按钮
user_name_login = driver.find_elements_by_css_selector('p.tang-pass-footerBarULogin')[0]
user_name_login.click()
time.sleep(3)

#输入账号与密码
user_name = driver.find_element_by_id("TANGRAM__PSP_10__userName")
user_name.send_keys("your_user_name")
time.sleep(3)
password = driver.find_element_by_id("TANGRAM__PSP_10__password")
password.send_keys("your_password")

#找到并点击登录按钮
denglu=driver.find_element_by_id('TANGRAM__PSP_10__submit')
denglu.click()
