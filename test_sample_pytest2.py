import time

import pytest
from selenium import webdriver
from test_sample_pytest import test_click


test_click()

@pytest.mark.valid
def test_gnail():
    driver=webdriver.Chrome()
    driver.get("https://mail.google.com/")
test_gnail()

@pytest.mark.invalid
def test_gmail():
    driver = webdriver.Chrome()
    driver.get("https://mail.google.com/")
    x=driver.title
    print(x)

test_gmail()
