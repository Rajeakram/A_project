"""from selenium import webdriver
import time

from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
time.sleep(2)
browser.get("https://www.dropbox.com/login")
browser.maximize_window()
time.sleep(2)
page_title=browser.title
print(page_title)
print(browser.title)


browser.get("https://reg.usps.com/login")
window_size=browser.set_window_size(width=1000,height=600)
time.sleep(3)

try:
    assert "yahoo" in page_title
    login("Yes,Its in there")
except AssertionError:
    print("AssertionError")
browser.back()
time.sleep(3)
x=browser.find_element(By.CLASS_NAME, "text-input-input")
if x is not None:
    print("Not in there")

browser.forward()
time.sleep(2)
print(browser.title)

print("Test Complete")"""
import time

"""from selenium import webdriver
import time
from selenium.webdriver.common.by import By
def login():
    driver=webdriver.Chrome()
    driver.get("https://www.bestbuy.com/identity/signin?token=tid%3A4a75ac26-b6cd-11ed-8219-0a1bb1c19fb1")
    driver.maximize_window()
    time.sleep(2)

    title=driver.title
    print(title)


    username=driver.find_element(By.CSS_SELECTOR,"input#fld-e")
    username.send_keys("94raje@gmail.com")
    time.sleep(3)

    show_password=driver.find_element(By.CSS_SELECTOR,".c-toggle-label")
    show_password.click()

    password=driver.find_element(By.CSS_SELECTOR,"input#fld-p1")
    password.send_keys("Raje433501!")
    time.sleep(3)

    login_click=driver.find_element(By.CSS_SELECTOR,"[type='submit']")
    login_click.click()
    time.sleep(3)

    x=driver.current_url
    print(x)
login()"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def ticket_purchse():
    driver=webdriver.Chrome()
    driver.get("https://www.expedia.com/Flights")
    time.sleep(3)
    driver.maximize_window()
    wait=WebDriverWait(driver,10)
    departing=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#location-field-leg1-origin-menu .uitk-form-field-trigger")))
    departing.send_keys("Nyc")
    go_country=wait.until(EC.presence_of_element_located((By.XPATH,"/html//div[@id='location-field-leg1-destination-menu']//button[@class='uitk-fake-input uitk-form-field-trigger']")))
    go_country.send_keys("Dhaka")
ticket_purchse()












