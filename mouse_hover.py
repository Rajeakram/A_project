"""import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

def mouse_hovar():
    driver=webdriver.Chrome()
    driver.get("https://www.apple.com/store")
    driver.maximize_window()
    wait=WebDriverWait(driver,10)
    explorer_product=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,".globalnav-link.globalnav-link-mac.globalnav-submenu-trigger-link > .globalnav-link-text-container")))
    action=ActionChains(driver)
    action.move_to_element(explorer_product).perform()
    time.sleep(3)
    try:
        sub_menu=wait.until(EC.presence_of_element_located((By.LINK_TEXT,"MacBook Air")))
        sub_menu.click()

        assert "Chase Checking Account" in driver.title
        print("YES")
    except:
        print("Kkj")
        time.sleep(5)
    print(driver.title)
mouse_hovar()"""
import time

"""import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def mouse_hover():
    driver=webdriver.Chrome()
    driver.get("https://www.apple.com/displays/")
    driver.maximize_window()

    ipad=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,".globalnav-link.globalnav-link-ipad.globalnav-submenu-trigger-link > .globalnav-link-text-container")))
    Action=ActionChains(driver)
    Action.move_to_element(ipad).perform()
    time.sleep(2)
    ipad_support=driver.find_element(By.LINK_TEXT,"iPad Support")
    ipad_support.click()
    search=driver.find_element(By.CSS_SELECTOR,"a#ac-gn-link-search")
    search.click()
    search = driver.find_element(By.CSS_SELECTOR, "input#ac-gn-searchform-input")
    search.send_keys("where is my Jupitar")
    search_submit=driver.find_element(By.CSS_SELECTOR,"button#ac-gn-searchform-submit")
    search_submit.click()
    time.sleep(2)

mouse_hover()"""

"""import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def mouse():
    driver=webdriver.Chrome()
    driver.get("https://www.samsung.com/us/")
    driver.maximize_window()
    mobile=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[data-index='0'] > [role]")))
    action=ActionChains(driver)
    action.move_to_element(mobile).perform()
    time.sleep(2)
    try:
        tablet=WebDriverWait(driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR,"[data-engname='mobile\:tablets']")))
        tablet.click()
        assert 'Samsung Galaxy tablets' in driver.title
        ptint('yes')
    except AssertionError:
        print("not")
    offer=driver.find_element(By.CSS_SELECTOR,"[aria-label='Offers']")
    offer.click()
    expected_url="https://www.samsung.com/us/tablets/#offers"
    expected_url=driver.current_url
    try:
        assert "https://www.samsung.com/us/tablets/#offers" in driver.current_url
        print("match")
    except:
        print("No")

    appliances=driver.find_element(By.CSS_SELECTOR,"ul:nth-of-type(1) > li:nth-of-type(3) > button[role='menuitem']")
    action.move_to_element(appliances).perform()
    refrigarator=driver.find_element(By.XPATH,"/html//nav[@id='component-id']//div[@class='nv00-gnb__l0-menu-wrap']/ul[1]/li[3]/div/div[2]/ul[@role='menu']/li[1]/a[@role='menuitem']")
    refrigarator.click()
    time.sleep(2)

mouse()"""

"""import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def mouse():
    drive=webdriver.Chrome()
    drive.get("https://www.samsung.com/us/")
    drive.get_window_size()
    drive.maximize_window()

    wait=WebDriverWait(drive,10)
    offers=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"[data-index='7'] button")))
    action=ActionChains(drive)
    action.move_to_element(offers).perform()

    try:
        mobile_and_table=wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Mobile and Tablet Trade-In"))).click()
        assert "https://www.samsung.com/us/trade-in/" in drive.current_url
        print("yes its in there ")
    except AssertionError:
        print("Nope")
mouse()"""
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def mousehover():
    driver=webdriver.Chrome()
    driver.get('https://www.samsung.com/us/')
    driver.maximize_window()
    wait=WebDriverWait(driver,10)
    accessories=wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"[data-index='5'] button")))
    print(driver.title)
    action=ActionChains(driver)
    action.move_to_element(accessories).perform()
    tv_acc=driver.find_element(By.LINK_TEXT,"All TV Accessories").click()
    expected_url="https://www.samsung.com/us/televisions-home-theater/television-home-theater-accessories/all-television-home-theater-accessories/?category_names=Televisions"
    actual_url=driver.current_url
    try:
        assert expected_url==actual_url
        print("yes")
    except:
        print("NO")

        driver.execute_script("window.open('https://www.apple.com/')")
        window=driver.window_handles
        print(window)
        print(driver.title)

    try:

        watch=wait.until(EC.presence_of_element_located((By.XPATH,"/html//ul[@id='globalnav-list']//div[@class='globalnav-menu-list']/div[5]/ul[@class='globalnav-submenu-trigger-group']//a[@href='https://www.apple.com/watch/']/span[@class='globalnav-link-text-container']")))
        action.move_to_element(watch).perform()
        shop_watch=wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Shop Apple Watch"))).click()
        time.sleep(2)
        print(driver.title)
    except:
          print("NO")


mousehover()









