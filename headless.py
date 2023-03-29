
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def headless():
    chrome_driver = Options()
    #chrome_driver.add_argument("--headless")#headless
    chrome_driver.add_argument("--window-size=400,300")#size
    chrome_driver.add_argument("--start-maximized")#maximize window
    chrome_driver.add_argument('--disable-extensions')#extension closed
    chrome_driver.add_argument('--incognito')#close all open tabs

    driver = webdriver.Chrome(options=chrome_driver)
    driver.get("https://www.yahoo.com/")
    time.sleep(3)
    driver.find_element(By.XPATH,"//html[@id='atomic']//input[@id='ybar-sbq']").send_keys("todays news")
    driver.find_element(By.CSS_SELECTOR,"button#ybar-search").click()
    expectedURL="https://search.yahoo.com/search?p=todays+news&fr=yfp-t&fr2=p%3Afp%2Cm%3Asb&ei=UTF-8&fp=1"
    actualUrl=driver.current_url
    time.sleep(1)
    if expectedURL==actualUrl:
        print("Match")
    else:
        print("NO")

headless()

"""import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def headless():
    chrome_driver=Options()
    chrome_driver.add_argument("--headless")
    driver=webdriver.Chrome(options=chrome_driver)
##
from selenium.webdriver.chrome.options import Options

chrome_drivre=Options()
chrome_drivre.add_argument("--headless")
drivre=webdriver.Chrome(options=chrome_drivre)"""
