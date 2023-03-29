import time
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def scroll():
    chrome_driver=Options()
    chrome_driver.add_argument("--incognito")
    driver=webdriver.Chrome(options=chrome_driver)
    url="https://www.apple.com/store"
    driver.get(url)
    driver.execute_script("window.scrollTo(0,1000)")
    driver.execute_script("window.scrollTo(0,0)")
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)
    orange=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[aria-label='HomePod - MidnightAvailable colors']")))

    driver.execute_script("agruments[0].scrollIntoView;",orange)
    time.sleep(3)
scroll()