import json
import time

from selenium import webdriver
import writeExcel
import csv

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\Users\15872\Desktop\chromedriver.exe")

def login(base_url):
    # PROXY = "112.2.26.50"
    driver.get(base_url)
    time.sleep(2)
    driver.execute_script('window.scrollTo(0, 200)')  # 遇见了反爬行为，通过滚动页面对抗
    username = "15052630374"
    password = "xw199810"
    driver.find_element_by_name('username').send_keys(username)
    time.sleep(2)
    driver.find_element_by_name('password').send_keys(password)
    time.sleep(5)
    # 点击登录
    driver.find_element_by_name('submit').click()
    cookies = driver.get_cookies()  # 获取cookie,列表形式
    print(cookies)
    f1 = open('cookies_bqg.txt', 'w')
    f1.write(json.dumps(cookies))
    f1.close()
    driver.close()
    # 退出，清除浏览器缓存


def getIn(url):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    time.sleep(2)
    cookies = [
        {"domain": "www.xbiquge.so", "expiry": 1741548660, "httpOnly": False, "name": "jieqiVisitInfo",
                  "path": "/","secure": False, "value": "jieqiUserLogin%3D1641548661%2CjieqiUserId%3D131855"},
        {"domain": "www.xbiquge.so", "expiry": 1644140661, "httpOnly": False, "name": "jieqiUserInfo", "path": "/",
          "secure": False,
          "value": "jieqiUserId%3D131855%2CjieqiUserUname%3D15052630374%2CjieqiUserName%3D15052630374%2CjieqiUs"
                   "erGroup%3D3%2CjieqiUserGroupName%3D%C6%D5%CD%A8%BB%E1%D4%B1%2CjieqiUserVip%3D0%2CjieqiUser"
                   "HonorId%3D%2CjieqiUserHonor%3D%D0%C2%CA%D6%C9%CF%C2%B7%2CjieqiUserPassword%3D67108618dc93"
                   "e4eaeee0644206be2686%2CjieqiUserUname_un%3D15052630374%2CjieqiUserName_un%3D15052630374%2"
                   "CjieqiUserHonor_un%3D%26%23x65B0%3B%26%23x624B%3B%26%23x4E0A%3B%26%23x8DEF%3B%2CjieqiUser"
                   "GroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%"
                   "3D1641548661"},
         {"domain": ".www.xbiquge.so", "httpOnly": False, "name": "Hm_lpvt_252f9a986eb5a291cc4f56bcecd88721",
          "path": "/", "secure": False, "value": "1641548667"},
         {"domain": "www.xbiquge.so", "httpOnly": False, "name": "PHPSESSID", "path": "/", "secure": False,
          "value": "sstkf2k52f7006vi32u0pk2d0a"},
        {"domain": ".www.xbiquge.so", "expiry": 1673084666, "httpOnly": False,
         "name": "Hm_lvt_252f9a986eb5a291cc4f56bcecd88721", "path": "/", "secure": False, "value": "1641548652"}]
    for cookie in cookies:
        print(cookie)
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)
    time.sleep(2)
    driver.refresh()
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/ul/li[9]/a').click()
    totalnum = driver.find_element_by_xpath('//*[@id="pagelink"]/a[14]').text
    for i in range(int(totalnum)):
        contents = driver.find_element_by_class_name('novelslistss').find_elements_by_tag_name("li")
        addContent = []
        for li in contents:
            spans = li.find_elements_by_tag_name('span')
            book_type = spans[0].text
            book_name = spans[1].text
            book_newElement = spans[2].text
            book_author = spans[3].text
            book_newTime = spans[4].text
            values_1 = [book_type, book_name, book_newElement, book_author, book_newTime]
            # addContent.append(values_1)
        # with open('test.csv', 'w+') as myFile:
        #     myWriter = csv.writer(myFile)
        #     myWriter.writerows(addContent) 方法一：保存到csv里
            writeExcel.Write_Excel.add_to_excel(self=newExcel, values=values_1)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 可以不加
        driver.find_element_by_class_name('next').click()

def newGet(url):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    time.sleep(2)
    cookies = [
        {"domain": "www.xbiquge.so", "expiry": 1741548660, "httpOnly": False, "name": "jieqiVisitInfo",
         "path": "/", "secure": False, "value": "jieqiUserLogin%3D1641548661%2CjieqiUserId%3D131855"},
        {"domain": "www.xbiquge.so", "expiry": 1644140661, "httpOnly": False, "name": "jieqiUserInfo", "path": "/",
         "secure": False,
         "value": "jieqiUserId%3D131855%2CjieqiUserUname%3D15052630374%2CjieqiUserName%3D15052630374%2CjieqiUs"
                  "erGroup%3D3%2CjieqiUserGroupName%3D%C6%D5%CD%A8%BB%E1%D4%B1%2CjieqiUserVip%3D0%2CjieqiUser"
                  "HonorId%3D%2CjieqiUserHonor%3D%D0%C2%CA%D6%C9%CF%C2%B7%2CjieqiUserPassword%3D67108618dc93"
                  "e4eaeee0644206be2686%2CjieqiUserUname_un%3D15052630374%2CjieqiUserName_un%3D15052630374%2"
                  "CjieqiUserHonor_un%3D%26%23x65B0%3B%26%23x624B%3B%26%23x4E0A%3B%26%23x8DEF%3B%2CjieqiUser"
                  "GroupName_un%3D%26%23x666E%3B%26%23x901A%3B%26%23x4F1A%3B%26%23x5458%3B%2CjieqiUserLogin%"
                  "3D1641548661"},
        {"domain": ".www.xbiquge.so", "httpOnly": False, "name": "Hm_lpvt_252f9a986eb5a291cc4f56bcecd88721",
         "path": "/", "secure": False, "value": "1641548667"},
        {"domain": "www.xbiquge.so", "httpOnly": False, "name": "PHPSESSID", "path": "/", "secure": False,
         "value": "sstkf2k52f7006vi32u0pk2d0a"},
        {"domain": ".www.xbiquge.so", "expiry": 1673084666, "httpOnly": False,
         "name": "Hm_lvt_252f9a986eb5a291cc4f56bcecd88721", "path": "/", "secure": False, "value": "1641548652"}]
    for cookie in cookies:
        print(cookie)
        if 'expiry' in cookie:
            del cookie['expiry']
        driver.add_cookie(cookie)
    time.sleep(2)
    driver.refresh()
    driver.get(url)
    totalnum = driver.find_element_by_class_name('last').text
    for i in range(int(totalnum)-340):
        contents = driver.find_element_by_class_name('novelslistss').find_elements_by_tag_name("li")
        addContent = []
        for li in contents:
            spans = li.find_elements_by_tag_name('span')
            book_type = spans[0].text
            book_name = spans[1].text
            book_newElement = spans[2].text
            book_author = spans[3].text
            book_newTime = spans[4].text
            values_1 = [book_type, book_name, book_newElement, book_author, book_newTime]
            # addContent.append(values_1)
            # with open('test.csv', 'w+') as myFile:
            #     myWriter = csv.writer(myFile)
            #     myWriter.writerows(addContent) 方法一：保存到csv里
            writeExcel.Write_Excel.add_to_excel(self=newExcel, values=values_1)
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 可以不加
        driver.find_element_by_class_name('next').click()

if __name__ == '__main__':
    # 模拟登陆-给定登陆的网址
    f = open('cookies_bqg.txt', 'r')
    newExcel = writeExcel.Write_Excel()
    cookies = f.read()
    if cookies == '':
        base_url = "https://www.xbiquge.so/login.php"
        login(base_url)
        print("笔趣阁登录成功！")
    else:
        # url = "https://www.xbiquge.so/"
        # # 可以直接进入需要爬的网页，这里先进入主页
        # getIn(url)
        # print("成功通过cookie进入笔趣阁")
        url = "https://www.xbiquge.so/top/allvisit/404.html"
        # 可以直接进入需要爬的网页，这里先进入主页
        newGet(url)
        print("成功通过cookie进入笔趣阁")
