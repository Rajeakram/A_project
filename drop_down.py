import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

def dropdown_check():
    driver=webdriver.Chrome()
    driver.get("https://www.salesforce.com/form/demo/salesforce-products/?gclid=CjwKCAiAu5agBhBzEiwAdiR5tCfpkTI3WSxTa1VDU9LKPeBn_jQWrOyAUvQbUzm7OyOT1JqEpv_GrxoCyWAQAvD_BwE&d=7010M000001ynfX&nc=7010M000002QR17&DCMP=KNC-Google&ef_id=CjwKCAiAu5agBhBzEiwAdiR5tCfpkTI3WSxTa1VDU9LKPeBn_jQWrOyAUvQbUzm7OyOT1JqEpv_GrxoCyWAQAvD_BwE:G:s&s_kwcid=AL!4604!3!605326008619!e!!g!!salesforce&gclsrc=aw.ds")
    time.sleep(2)
    driver.maximize_window()
    print(driver.title)
    time.sleep(3)

    wait=WebDriverWait(driver,10)
    dropdown=Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"[name='CompanyCountry']"))))
    print(dropdown)
    #default=dropdown.first_selected_option
    dropdown.select_by_index("5")
    time.sleep(2)

dropdown_check()
