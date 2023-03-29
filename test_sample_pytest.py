import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login():
    driver= webdriver.Chrome()
    driver.get("https://www.yahoo.com/")
    time.sleep(2)
    print(driver.title)
test_login()

def test_click():
    driver = webdriver.Chrome()
    driver.get("https://www.yahoo.com/")
    time.sleep(2)
    print(driver.title)
    driver.find_element(By.CSS_SELECTOR,"[name='p']").send_keys("my name jamal")
test_click()
