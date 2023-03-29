"""from selenium import webdriver
import time

from selenium.webdriver.common.by import By

browser=webdriver.Chrome()
time.sleep(2)
browser.get("https://www.dropbox.com/login")
browser.maximize_window()
time.sleep(2)
page_title=browser.title
print(page_title)
print(browser.title)


browser.get("https://reg.usps.com/login")
window_size=browser.set_window_size(width=1000,height=600)
time.sleep(3)

try:
    assert "yahoo" in page_title
    login("Yes,Its in there")
except AssertionError:
    print("AssertionError")
browser.back()
time.sleep(3)
x=browser.find_element(By.CLASS_NAME, "text-input-input")
if x is not None:
    print("Not in there")

browser.forward()
time.sleep(2)
print(browser.title)

print("Test Complete")"""
import time

"""from selenium import webdriver
import time
from selenium.webdriver.common.by import By
def login():
    driver=webdriver.Chrome()
    driver.get("https://www.bestbuy.com/identity/signin?token=tid%3A4a75ac26-b6cd-11ed-8219-0a1bb1c19fb1")
    driver.maximize_window()
    time.sleep(2)

    title=driver.title
    print(title)


    username=driver.find_element(By.CSS_SELECTOR,"input#fld-e")
    username.send_keys("94raje@gmail.com")
    time.sleep(3)

    show_password=driver.find_element(By.CSS_SELECTOR,".c-toggle-label")
    show_password.click()

    password=driver.find_element(By.CSS_SELECTOR,"input#fld-p1")
    password.send_keys("Raje433501!")
    time.sleep(3)

    login_click=driver.find_element(By.CSS_SELECTOR,"[type='submit']")
    login_click.click()
    time.sleep(3)

    x=driver.current_url
    print(x)
login()"""

"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def ticket_purchse():
    driver=webdriver.Chrome()
    driver.get("https://www.expedia.com/Flights")
    time.sleep(3)
    driver.maximize_window()
    wait=WebDriverWait(driver,10)
    departing=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#location-field-leg1-origin-menu .uitk-form-field-trigger")))
    departing.send_keys("Nyc")
    go_country=wait.until(EC.presence_of_element_located((By.XPATH,"/html//div[@id='location-field-leg1-destination-menu']//button[@class='uitk-fake-input uitk-form-field-trigger']")))
    go_country.send_keys("Dhaka")
ticket_purchse()"""

import time

"""from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


def select_dropdown():

    driver = webdriver.Chrome()
    driver.get("https://the-internet.herokuapp.com/dropdown")

    dropdown = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "dropdown"))))

    default_selected_option = dropdown.first_selected_option
    try:
        assert default_selected_option.is_selected, "Please select an option"
        print("Test Case 1: Test passed.'Please select an option' is selected as default. Test passed.")

    except AssertionError:
        print("Test Case 1: Test failed.'Please select an option' is not selected as default. Test failed.")


    dropdown.select_by_visible_text("Option 2")
    new_selected_option = dropdown.first_selected_option

    try:
        assert new_selected_option.is_selected, "Option 2"
        print("Test Case 2: Test passed.Option 2 is new selected. Test passed.")

    except AssertionError:
        print("Test Case 2: Test failed.Option 2 is not new selected. Test failed.")


    expected_options_list = ["Please select an option", "Option 1", "Option 2"]
    actual_options_list = []


    for opt in dropdown.options:
        options_text = opt.text
        actual_options_list.append(options_text)


    try:
        assert actual_options_list == expected_options_list
        print("Test Case 3: Test passed.All Options Available.Test passed")
    except AssertionError:
        print("Test Case 3: Test failed.All Options not Available.Test failed")


    driver.close()


select_dropdown()"""

"""import time
from selenium import webdriver

def multiweb():
    driver=webdriver.Chrome()
    driver.get("https://www.youtube.com/watch?v=YlwzjyvSe2w")
    time.sleep(1)
    driver.execute_script("window.open('https://www.samsung.com/us/tablets/#offers')")
    windows=driver.window_handles
    print(windows)

    driver.switch_to.window(windows[0])
    print(driver.title)
    time.sleep(1)

multiweb()"""
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
def final():
    driver=webdriver.Chrome()
    driver.get("https://www.samsung.com/us/")
    driver.maximize_window()
    time.sleep(1)
    parent_handle=driver.current_window_handle
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.apple.com/")
    driver.set_window_size(700,500)
    driver.maximize_window()
    print(driver.title)
    time.sleep(1)
    driver.back()
    expected_url="https://www.samsung.com/us/"
    actual_url=driver.current_url
    try:
        assert expected_url==actual_url
        print("Match")
    except:
        print("NOPE")


    search=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".gnb__search-btn-js.nv00-gnb__utility-btn > svg[role='presentation']")))
    search.click()
    inpuut=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#gnb-search-keyword"))).send_keys("S3")
    hit=driver.find_element(By.CSS_SELECTOR,"[an-tr='search layer--Image-submit'] [focusable]")
    hit.click()
    time.sleep(2)


    driver.forward()#does not forward to the apple page
    print(driver.title)
    time.sleep(2)
    print(driver.current_url)#why i have wrong url



    driver.execute_script("window.open('https://www.apple.com/')")
    child = driver.window_handles
    for handle in child:
        if handle != parent_handle:
            driver.switch_to.window(handle)
            applesearch=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".globalnav-link.globalnav-link-entertainment.globalnav-submenu-trigger-link > .globalnav-link-text-container")))
            action=ActionChains(driver)
            action.move_to_element(applesearch).perform()
            time.sleep(2)
            appleinput=driver.find_element(By.CSS_SELECTOR,"div#globalnav-submenu-link-entertainment .globalnav-submenu-group.globalnav-submenu-group-elevated > .globalnav-submenu-list > li:nth-of-type(1) > .globalnav-submenu-link")
            appleinput.click()

    driver.execute_script("window.open('https://www.yahoo.com/')")
    newtab=driver.switch_to.window(driver.window_handles[2])
    print(newtab)
    small_business=wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Sign in")))
    small_business.click()
    time.sleep(2)
final()














