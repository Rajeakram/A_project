"""import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def multiple_window():
    driver=webdriver.Chrome()
    driver.get("https://www.samsung.com/us/tablets/#offers")
    driver.execute_script("window.open('https://apple.com')")
    time.sleep(2)
    driver.execute_script("window.open('https://material.angular.io/cdk/dialog/overview')")
    time.sleep(2)

    total_windows = driver.window_handles
    print(total_windows)

    driver.switch_to.window(total_windows[1])
    time.sleep(2)
    driver.switch_to.window(total_windows[0])
    time.sleep(2)
multiple_window()"""


