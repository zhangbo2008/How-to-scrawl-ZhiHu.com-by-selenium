import os
import pickle
import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
options = webdriver.ChromeOptions()
chrome_options = options
# chrome_options.add_argument("--headless")
options.add_experimental_option('excludeSwitches', ['enable-automation'])
brower = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(brower, 10)


def getZhihuCookies():
    # get login Zhihu cookies
    url = "https://www.Zhihu.com/"
    loginUrl = "https://www.zhihu.com/signin?next=%2F"
    brower.get(loginUrl)


    while True:
        print("Please login in Zhihu.com!")
        time.sleep(3)
        # if login in successfully, url  jump to www.Zhihu.com

        if checkLogin(brower, loginUrl):
            tbCookies = brower.get_cookies()
            print(tbCookies)
            # brower.quit()
            cookies = {}
            for item in tbCookies:
                cookies[item['name']] = item['value']
            outputPath = open('ZhihuCookies.pickle', 'wb')
            pickle.dump(cookies, outputPath)
            outputPath.close()
            return cookies

def checkLogin(brower, loginUrl=None):
    return str(brower.current_url).find("signin") == -1

def readZhihuCookies():
    # if hava cookies file ,use it
    # if not , getZhihuCookies()
    if os.path.exists('ZhihuCookies.pickle'):
        readPath = open('ZhihuCookies.pickle', 'rb')
        print("start pickle.load")
        tbCookies = pickle.load(readPath)
        print("end pickle.load")
    else:
        tbCookies = getZhihuCookies()
    return tbCookies


def main():
    tbCookies = readZhihuCookies()
    print("1111111111111111111111")
    print(tbCookies,"真正的cookie是这个")
    brower.get("https://www.Zhihu.com")
    for cookie in tbCookies:
        brower.add_cookie({
            "domain": ".zhihu.com",
            "name": cookie,
            "value": tbCookies[cookie],
            "path": '/',
            "expires": None
        })
    a=brower.get("https://www.Zhihu.com")
    print(a,9999999999999999999999999999999)
    time.sleep(111111111111)


main()