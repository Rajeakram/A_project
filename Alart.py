import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def alart():
    driver=webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    wait=WebDriverWait(driver,10)
    alart=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH, "//div[@id='content']//ul//button[.='Click for JS Alert']")))
    alart.click()
    time.sleep(3)
    alart_verify=wait.until(EC.alert_is_present())
    try:
        assert alart_verify.text=="I am a JS Alert"
        print("Test Passed")
    except AssertionError:
        print("Test passed")
    alart_verify.accept()


    alart_confirm=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//div[@id='content']//ul//button[.='Click for JS Confirm']")))
    alart_confirm.click()
    time.sleep(2)
    alart_confirm_verify=wait.until(EC.alert_is_present())
    try:
        assert alart_confirm_verify.text=="I am a JS Confirm"
        print("yes its in there")
    except AssertionError:
        print("false")
    alart_confirm_verify.dismiss()
    time.sleep(1)


    alart_confirm_promot = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//div[@id='content']//ul//button[.='Click for JS Prompt']")))
    time.sleep(3)
    alart_confirm_promot.click()
    time.sleep(2)
    alart_confirm_promot_verify = wait.until(EC.alert_is_present())
    try:
        assert alart_confirm_promot_verify.text == "I am a JS prompt"
        alart_confirm_promot_verify.send_keys("sfdgdg")
        print("yes its in there")
    except AssertionError:
        print("false")
    alart_confirm_promot_verify.accept()

    time.sleep(3)


alart()
