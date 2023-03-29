"""import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def drag_drop():
    driver=webdriver.Chrome()
    driver.get("https://material.angular.io/cdk/drag-drop/examples")
    driver.maximize_window()
    wait=WebDriverWait(driver,10)
    source=wait.until(EC.presence_of_element_located((By.XPATH,"//example-viewer[@id='cdk-drag-drop-axis-lock']//cdk-drag-drop-axis-lock-example[@class='ng-star-inserted']/div[1]")))
    target=driver.find_element(By.CSS_SELECTOR,"cdk-drag-drop-axis-lock-example .example-box:nth-of-type(2)")
    action=ActionChains(driver)
    action.drag_and_drop(source,target).perform()
    time.sleep(3)
drag_drop()"""


"""import time
from selenium import webdriver
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


def drag_and_drop():
    # Step1: launch the browser
    driver = webdriver.Chrome()

    # Step2: Go to page
    driver.get("https://material.angular.io/cdk/drag-drop/examples")
    time.sleep(5)

    source_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "example-viewer#cdk-drag-drop-custom-placeholder .cdk-drop-list.example-list > div:nth-of-type(1)")))

    target_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "example-viewer#cdk-drag-drop-custom-placeholder .cdk-drop-list.example-list > div:nth-of-type(2)")))

    actions = ActionChains(driver)

    actions.drag_and_drop(source_element, target_element).perform()


drag_and_drop()"""

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def drag_and_drop():
    driver=webdriver.Chrome()
    driver.get("https://material.angular.io/cdk/drag-drop/examples")
    source=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"cdk-drag-drop-axis-lock-example .example-box:nth-of-type(2)")))
    target=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"cdk-drag-drop-axis-lock-example .example-box:nth-of-type(1)")))
    action=ActionChains(driver)
    action.drag_and_drop(source,target).perform()
drag_and_drop()

