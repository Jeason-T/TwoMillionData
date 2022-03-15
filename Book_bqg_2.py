import json
import time

from selenium import webdriver
import writeExcel
import csv

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\Users\15872\Desktop\chromedriver.exe")
url_temp = ''


def getIn(url):
    driver.get(url)
    driver.implicitly_wait(10)
    # totalnum = driver.find_element_by_xpath('//*[@id="pagelink"]/a[14]').text
    for i in range(2761):
        try:
            contents = driver.find_element_by_xpath('//*[@id="articlelist"]/ul[2]').find_elements_by_tag_name('li')
            addContent = []
            for li in contents:
                spans = li.find_elements_by_tag_name('span')
                book_type = spans[0].text
                book_name = spans[1].text
                book_author = spans[2].text
                book_newElement = spans[3].text
                book_allNumber = spans[4].text
                book_newTime = spans[6].text
                values_1 = [book_type, book_name, book_author, book_newElement, book_allNumber, book_newTime]
                # addContent.append(values_1)
                # with open('test.csv', 'w+') as myFile:
                #     myWriter = csv.writer(myFile)
                #     myWriter.writerows(addContent) 方法一：保存到csv里
                writeExcel.Write_Excel.add_to_excel(self=newExcel, values=values_1)
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 可以不加
            driver.find_element_by_class_name('next').click()
        except:
            driver.refresh()
            print('刷新了一遍网页')

if __name__ == '__main__':
    # 模拟登陆-给定登陆的网址
    # url = "https://www.xbiquge.so/"
    # # 可以直接进入需要爬的网页，这里先进入主页
    # getIn(url)
    # print("成功通过cookie进入笔趣阁")
    newExcel = writeExcel.Write_Excel()
    # 出现 错误 重新开始
    url = "https://www.bbiquge.net/top/allvisit/2217.html"
    # 可以直接进入需要爬的网页，这里先进入主页
    getIn(url)
    print("数据获取成功")
