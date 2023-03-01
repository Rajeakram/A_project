from selenium import webdriver
import time
from selenium.webdriver.common.by import By
def login():

    # open browser
    browser=webdriver.Chrome()

    # Put the url where we want to login
    browser.get("https://www.bestbuy.com/identity/signin?token=tid%3A74ccde55-b6c1-11ed-8b6e-12b1239627a5")
    time.sleep(3)
    browser.maximize_window()

    #find element and  input keys
    username=browser.find_element(By.ID, "fld-e")
    username.send_keys("94raje@gmail.com")
    time.sleep(3)

    password=browser.find_element(By.NAME, "fld-p1")
    password.send_keys("Raje433501!")
    time.sleep(3)

    submit=browser.find_element(By.CSS_SELECTOR,"[type='submit']")
    submit.click()
    time.sleep(3)

    expected_url="https://www.bestbuy.com/identity/signin/twoStepVerification?token=tid%3Aaff86edc-b6c5-11ed-bfbd-0ef3c8a895d9"
    actual_url=browser.current_url
    try:
        assert expected_url==actual_url
        print("Match")
    except AssertionError:
        print('Doesnt Match')


login()



