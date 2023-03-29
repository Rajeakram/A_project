import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



driver=webdriver.Chrome()
driver.get("https://signin.swagup.com/")
wait=WebDriverWait(driver,10)
time.sleep(2)
signup=wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,"a[title='Sign up']")))
signup.click()
if "https://signin.swagup.com/signin/register" in driver.current_url:
    print("yes its correct")
else:
    print("it does not match")

username=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name='email']")))
username_display=username.is_displayed()
time.sleep(2)
try:
    assert username_display==True
    username.send_keys("shalehakramraje@yahoo.com")
except:
     print("dont find the answer")
password=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"input[name='password']")))
password.send_keys("Xyz4321!")
time.sleep(2)
company=wait.until(EC.presence_of_element_located((By.XPATH,"//main[@id='okta-sign-in']//form[@action='/signin/register']/div[1]/div[@class='o-form-fieldset-container']/div[4]//input[@name='organization']")))
company.send_keys("Jay Jay")
time.sleep(2)
first_name=wait.until(EC.presence_of_element_located((By.XPATH,"//main[@id='okta-sign-in']//form[@action='/signin/register']/div[1]/div[@class='o-form-fieldset-container']/div[5]//input[@name='firstName']")))

try:
    assert first_name.is_displayed()
    first_name.send_keys("jaman")
except AssertionError:
     print("No Field")
time.sleep(2)

last_name=wait.until(EC.presence_of_element_located((By.XPATH,"//main[@id='okta-sign-in']//form[@action='/signin/register']/div[1]/div[@class='o-form-fieldset-container']/div[6]//input[@name='lastName']")))
last_name.send_keys("kamal")
time.sleep(2)

register=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"[type='submit']")))
register.click()
time.sleep(2)
"""try:
   assert register.is_enable()
    register.click()
except AssertionError:
    print("Sorry")"""







