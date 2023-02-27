"""To find a locator in selenium we follow some ways;
Id, Name, ClassName, tag Name , TagName , Link Text, PartioLinkText ,CSS, Xpath"""
from selenium.webdriver.common.by import By

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
driver.get("https://enroll.getcovered.nj.gov/hix/account/user/login")
time.sleep(2)

#find username input field

x=driver.find_element(By.ID, "j_username")
if x is not None:
    print("it is correct")
#find Password input field
y=driver.find_element(By.ID, "j_password")
if y is not None:
    print("Yes")
#find login input field
z=driver.find_element(By.ID, "submit")
if z is not None:
    print("Yahoo")

print("Test Pass")


from selenium import webdriver
import time

driver=webdriver.Edge()
driver.maximize_window()
time.sleep(2)
driver.get("https://myturbotax.intuit.com/")
time.sleep(2)

X = driver.find_element(By.NAME, "Email")
if X is not None:
    print("YES")




