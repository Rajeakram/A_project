A="akram"
print(type(A))

a ="jaman is a good boy but he smokes ciggarate"
print(a.find("is"))
if "is"not in "a":
    print("yes it is")
else:
    print("NO")
a = 5
def x():
    global c
    c = 10
    print(a+c)
x()

from selenium import webdriver
import time

browser=webdriver.Chrome()
browser.maximize_window()
browser.get("https://drive.google.com/drive/folders/1RluFmi4IfggyD54btvecun9TI3LL1klW?fbclid=IwAR0kJaDChxlF1cH6KqWxn6ea5sq9xQzoxuCIXP-bEL4P9aI8wvxe73WpPps")
title=browser.title # web page title name fetching
print(title)

try:
    assert "Google" in browser.title # to verify title name is correct or not
except AssertionError: # "try" and "except" use for if title gets wrong then testing will not stop if use try and except
    print(str(AssertionError))

time.sleep(4)
print("test complete")