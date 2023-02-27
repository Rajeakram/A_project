from selenium import webdriver
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

print("Test Complete")


