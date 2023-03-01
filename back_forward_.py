from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://www.yahoo.com/")
time.sleep(3)

browser.get("https://www.youtube.com/")
time.sleep(3)

browser.back()
print(browser.title)
time.sleep(2)

browser.forward()
time.sleep(2)
print(browser.title)


browser.refresh()
print("Test Execution Has been completed")

"""This is for Going back to previous page ,
Forward page , and refreshing a page"""