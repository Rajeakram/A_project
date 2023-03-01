from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def wait():
    # Step1: launch the browser
    driver = webdriver.Chrome()

    # Step2: Go to Login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Step3: Enter Username
    username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "username")))

    # Verify username is Displayed in login page
    username_display_state=username.is_displayed()
    try:
        assert username_display_state==True
        username.send_keys("Admin")
    except AssertionError:
        print("Username is not available")

    # Step4: Enter Password
    Password = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))
    Password_verify=Password.is_enabled()

    # Verify password is Enabled in login page
    try:
        assert Password.is_enabled()==True
        Password.send_keys("admin123")
    except AssertionError:
        print("Password is not enabled")

    # Step5: Click Login button
    LoginButton = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".orangehrm-login-button")))
    login_verify=LoginButton.is_enabled()

    # Verify LoginButton is Disabled in login page
    try:
        assert LoginButton.is_enabled()==True
        LoginButton.click()
    except AssertionError:
        print("Login Button is not Enabled")

    # Step6: Expected Result : Verify by URL
    ExpectedURL = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

    # Step7: Actual Result : Verify by URL
    ActualURL = driver.current_url

    # Step8: Test Result
    try:
        assert ExpectedURL == ActualURL
        print("Valid Test Case Result: Passed")
    except AssertionError:
        print("Valid Test Case Result: Failed")

    # Step9: Close the browser
    driver.close()


wait()