"""import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


def upload():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/upload")
    driver.maximize_window()
    driver.get_window_size()

    chooseFile=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,"file-upload"))).send_keys("E:\Book1.xlsx")

    up=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"input#file-submit")))
    up.click()
    time.sleep(2)


upload()"""

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def upload():
    driver=webdriver.Chrome()
    driver.get("https://www.simpleimageresizer.com/")
    driver.maximize_window()
    wait=WebDriverWait(driver,10)

    image=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"[value='Select image']")))
    image.send_keys("E:\download.jpg")
    time.sleep(2)
    resize=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"[value='Resize']"))).click()
    time.sleep(5)


upload()
