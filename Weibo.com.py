import json
import time

from selenium import webdriver
import writeExcel
import csv

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\Users\15872\Desktop\chromedriver.exe")
url_temp = ''

def login(base_url):
    # PROXY = "112.2.26.50"
    driver.get(base_url)
    driver.maximize_window()
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="__sidebar"]/div/div[1]/div[1]/div/button').click()
    # 点击登录
    time.sleep(10)
    # 预留时间用来手机登录
    cookies = driver.get_cookies()  # 获取cookie,列表形式
    print(cookies)
    f1 = open('cookie_weibo.txt', 'w')
    f1.write(str(cookies))
    f1.close()
    getData(driver)
    # 退出，清除浏览器缓存

def login_Cookie(url):
    f1 = open('cookie_weibo.txt', 'r')
    cookie_temp = f1.read()
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    time.sleep(2)
    cookies = cookie_temp
    for cookie in cookies:
        print(cookie)
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)
    time.sleep(2)
    driver.refresh()
    driver.get(url)
    time.sleep(15)
    getData(driver)

def getData(driver):
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[1]/div/div[1]/div/div/div[2]/div/div[1]/a[3]/div/div[1]'
                                 '/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="app"]/div[1]/div[2]/div[1]/div/div/div/div/a[3]/div').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="scroller"]/div[1]/div[1]/div/div/a/div/div/div[1]/div[1]/div[2]').click()
    time.sleep(3)

    contents=driver.find_element_by_xpath('//*[@id="pl_feedlist_index"]/div[3]')\
        .find_elements_by_class_name('card-wrap')

    print(contents)

    for content in contents[1:]:
        print('++++++++++')
        print(content)
        content_txt = content.find_element_by_xpath('//*[@id="pl_feedlist_index"]/div[4]/div[1]/div[2]'
                                                    '/div[1]/div[2]/p[2]').text
        print(content_txt)

if __name__ == '__main__':
    url = "https://weibo.com"
    # 可以直接进入需要爬的网页，这里先进入主页
    login(url)
    # login_Cookie(url)
    # 两种登录的方式，具体使用哪种看具体情形

    # print("使用cookie登录成功")
    print("数据获取成功")
