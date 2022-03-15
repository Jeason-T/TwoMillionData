import json
import time

from selenium import webdriver


def login(base_url):
    # PROXY = "112.2.26.50"
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server={0}'.format(PROXY))
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\Users\15872\Desktop\chromedriver.exe")

    # driver.add_cookie('WEIBOCN_FROM=1110006030; SUB=_2A25M0RCgDeRhGeFI4lYW8ijFyD2IHXVsPbDorDV6PUJbktCOLUvGkW1NfNAuP00PL'
    #                   'RGGjG7x4iLD172LEODxbUdw; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhxjaQbE4bKcyGApSFbRlHj5NHD95QNSo'
    #                   '.XS0zc1KepWs4DqcjMi--NiK.Xi-2Ri--ciKnRi-zNS0q4ShMESo.0eBtt; SSOLoginState=1641373936; MLOGIN=1; '
    #                   '_T_WM=44190106647; XSRF-TOKEN=62499f; M_WEIBOCN_PARAMS=luicode%3D20000174%26uicode%3D20000174')
    # print(driver.page_source)

    time.sleep(2)
    driver.execute_script('window.scrollTo(0, 200)')  # 遇见了反爬行为，通过滚动页面对抗
    username = "18082325097"
    password = "xw199810"
    driver.find_element_by_css_selector('#loginName').send_keys(username)
    time.sleep(2)
    driver.find_element_by_css_selector('#loginPassword').send_keys(password)
    time.sleep(2)
    # 点击登录
    driver.find_element_by_css_selector('#loginAction').click()

    time.sleep(30)
    cookies = driver.get_cookies()  # 获取cookie,列表形式
    print(cookies)
    f1 = open('cookies.txt', 'w')
    f1.write(json.dumps(cookies))
    f1.close()
    driver.close()
    # 退出，清除浏览器缓存


def getIn(url):
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server={0}'.format(PROXY))
    driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=r"C:\Users\15872\Desktop\chromedriver.exe")
    driver.get(url)
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    time.sleep(5)
    cookies = {
        {'domain': '.weibo.cn', 'expiry': 1673007402, 'httpOnly': True, 'name': 'SUB', 'path': '/', 'sameSite': 'None',
         'secure': True, 'value': '_2A25M0q36DeRhGeFI4lYW8ijFyD2IHXVsPDOyrDV6PUJbk'
                                  'tCOLXfVkW1NfNAuP2FuOXrEFrjwXm9SZulUuGgxIrO4'},
        {'domain': '.weibo.cn', 'expiry': 1673007402, 'httpOnly': False, 'name': 'SUBP', 'path': '/',
         'sameSite': 'None', 'secure': True,
         'value': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WhxjaQbE4bKcyGApSFbRlHj5NHD95QNSo.XS0zc1KepWs4DqcjMi--NiK.Xi-2Ri--'
                  'ciKnRi-zNS0q4ShMESo.0eBtt'},
        {'domain': '.weibo.cn', 'httpOnly': False, 'name': 'SSOLoginState', 'path': '/', 'sameSite': 'None',
         'secure': True, 'value': '1641471402'},
        {'domain': '.weibo.cn', 'expiry': 1641484800, 'httpOnly': False, 'name': '_T_WM', 'path': '/', 'secure': False,
         'value': '50017706970'},
        {'domain': '.weibo.cn', 'httpOnly': True, 'name': 'WEIBOCN_FROM', 'path': '/', 'secure': False,
         'value': '1110006030'},
        {'domain': '.weibo.cn', 'expiry': 1641475003, 'httpOnly': False, 'name': 'MLOGIN', 'path': '/', 'secure': False,
         'value': '1'},
        {'domain': '.m.weibo.cn', 'expiry': 1641472603, 'httpOnly': False, 'name': 'XSRF-TOKEN', 'path': '/',
         'secure': False, 'value': '70d093'},
        {'domain': '.weibo.cn', 'expiry': 1641472003, 'httpOnly': True, 'name': 'M_WEIBOCN_PARAMS', 'path': '/',
         'secure': False, 'value': 'uicode%3D20000174'},

    }

    driver.add_cookie(cookies)
    for cookie in cookies:
        # if 'expiry' in cookie:
        #     del cookie['expiry']
        driver.add_cookie(cookie)
    time.sleep(5)
    driver.refresh()
    driver.get(url)


if __name__ == '__main__':
    # 模拟登陆-给定登陆的网址
    # base_url = "https://passport.weibo.cn/signin/login"
    # login(base_url)
    # print("新浪微博登陆成功！")

    url = "https://m.weibo.cn/"
    getIn(url)
    print("成功通过cookie登录微博")
