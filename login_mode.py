from selenium import webdriver
import time
import os
from config import config

config = config()

def driverPath(url = config.get('ip', 'url')):
    currentPath = os.path.dirname(os.path.realpath(__file__))
    options = webdriver.ChromeOptions()
    #數字0代表載時不要跳出視窗，而是直接下載。改成數字1的話則會跳出視窗
    #預設路徑為當前目錄的下一層，名為Downloads的資料夾。如果沒有名為Downloads的資料夾便會新增一個

    prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': currentPath + '\\Downloads'}
    options.add_experimental_option('prefs', prefs)
    #設定下載檔案的預設路徑
    
    chromedriver_path = currentPath + '\\chromedriver.exe'
    print(chromedriver_path)
    try:
        driver = webdriver.Chrome(executable_path = chromedriver_path, chrome_options = options)
        #driver = webdriver.Chrome(currentPath + '\chromedriver.exe')
        driver.get(url)
    except Exception as err:
        print(err)
    return driver


def login(driver):
    
    time.sleep(2)
    driver.find_element_by_id('textfield-1022-inputEl').send_keys('user@onwardsecurity.com')
    driver.find_element_by_id('textfield-1023-inputEl').send_keys('12345678')
    time.sleep(1)
    #點擊「登入」
    driver.find_element_by_xpath('/html[1]/body[1]/div[5]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/a[1]').click()   
    time.sleep(3)