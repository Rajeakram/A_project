from selenium import webdriver
import time
from selenium.webdriver.common.by import By

def login():
    driver=webdriver.Chrome()
    driver.get("https://signin.swagup.com/")
    time.sleep(2)
    print(driver.title)

    username=driver.find_element(By.CSS_SELECTOR,"#okta-signin-username")
    username_verify=username.is_enabled()
    try:
        assert username_verify==True
        username.send_keys("Shalehraraje@yahoo.com")
        time.sleep(3)
    except:
        print("Error")


    password=driver.find_element(By.ID,"okta-signin-password")
    password_verify=password.is_displayed()
    try:
        assert password_verify==True
        password.send_keys("Jbahjhbsj367236542")
        time.sleep(3)
    except:
        print("Error")

    signin=driver.find_element(By.XPATH,"/html//input[@id='okta-signin-password']")
    singin_verify=signin.is_enabled()
    try:
        assert singin_verify==True
        signin.click()
        time.sleep(3)
    except:
        print("error")

    print(driver.title)
login()
