import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options

def final():
    chrome_driver=Options()
    chrome_driver.add_argument("--incognito")#headless
    driver=webdriver.Chrome(options=chrome_driver)
    url="https://alphaprimetech.org/?gclid=Cj0KCQjw8e-gBhD0ARIsAJiDsaVNOQlzxJjmY_szitU5vlH-4ls7AsbyeX6KO_xoJ4rOOpHLJC_h8xsaAmexEALw_wcB"
    driver.get(url)
    parent_window=driver.current_window_handle
    handles=driver.window_handles
    driver.maximize_window()#window maximize
    time.sleep(3)
    expected_title="Leading Career Training School in Manhattan, New York | AlphaPrimeTech"
    actul_title=driver.title
    try:
        assert expected_title==actul_title
    except:
        print("its not it")

    wait=WebDriverWait(driver,10)#find element and send keys
    name=wait.until(EC.presence_of_element_located((By.NAME,"firstname"))).send_keys("Raje")

    time.sleep(2)
    driver.refresh()
    time.sleep(3)
    name = wait.until(EC.presence_of_element_located((By.NAME, "firstname")))
    name_verify=name.is_enabled()#state define
    try:
        assert name_verify==True
        name.send_keys("Raje")
        time.sleep(3)
    except AssertionError:
        print("Not displayable")
    robot=driver.find_element(By.XPATH,"/html/body")
    robot_verify=robot.is_enabled()
    try:
        assert robot_verify==True
        robot.click()
    except:
        print("error")

    field_of_Study=Select(wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"select#studycourse"))))
    field_of_Study.select_by_index("2")   #drop down
    time.sleep(2)
    training_course=driver.find_element(By.LINK_TEXT,"TRAINING COURSES")
    action=ActionChains(driver)
    action.move_to_element(training_course).perform()
    ba=driver.find_element(By.CSS_SELECTOR,"ul#menu-top-navigation > .list_mega_menu.menu-item.menu-item-463.menu-item-has-children.menu-item-object-page.menu-item-type-post_type  .menu-item.menu-item-1568.menu-item-has-children.menu-item-object-custom.menu-item-type-custom .menu-image-title.menu-image-title-after")
    ba.click()
    time.sleep(2)
    driver.execute_script("window.open('https://www.apple.com/store')")
    driver.switch_to.window(driver.window_handles[1])#window control
    product=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"a#globalnav-menubutton-link-search")))
    product.click()
    driver.find_element(By.CSS_SELECTOR,"[placeholder]").send_keys("hdsjhdvf")
    time.sleep(3)

    """login=driver.find_element(By.CSS_SELECTOR,".globalnav-wrapper-c360 > hgf-c360nav")
    action=ActionChains(driver)
    action.move_to_element(login).perform()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,".globalnav-wrapper-c360 > hgf-c360nav").click()
    print(driver.title)
    time.sleep(2)"""
final()
