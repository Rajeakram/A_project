from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver=webdriver.Chrome()
driver.get("https://signin.swagup.com/")
username=WebDriverWait(driver, 10).until(EC.(driver.find_element(By.CSS_SELECTOR,"input#okta-signin-username")))
username_display=username.is_displayed()
try:
    assert username_display==True
    username.send_keys("shalehakramraje@yahoo.com")
except:
     print("dont find the answer")





